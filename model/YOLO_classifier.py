import cv2
from ultralytics import YOLO
import os
from tqdm import tqdm
class YoloClassifier():
    def __init__(self,img_folder, single_img_file_name, video_folder, video_name, model_path):
        # 1. 传入参数：检测图片文件夹，图片名称，检测视频文件夹，视频名称，模型 均为根目录下路径（root/)
        # 2. 保存至结果文件夹 data_savefold/images&data_savefold/videos 
        # 3. 返回结果文件夹 文件名 路径
        self.img_folder = img_folder # 'YOLOclassifier_data/images'  
        self.single_img_file_name = single_img_file_name # *.jpg
        self.video_folder = video_folder #'YOLOclassifier_data/videos'  
        self.video_name = video_name # *.mp4
        self.img_save_folder='data_savefold/images'
        self.video_save_folder='data_savefold/videos'
        self.model = YOLO(model_path)

    def classifyOneImg(self):
        img_path = self.img_folder+'/'+self.single_img_file_name# .../*.jpg
        if not os.path.isfile(img_path):  
            raise FileNotFoundError(f"File {self.single_img_file_name} not found.")  
        img = cv2.imread(img_path)
        res = self.model.predict(source = img,save=False)
        resimg = res[0].plot()
        # 图片存储路径
        save_path = self.img_save_folder + "/"+self.single_img_file_name
        if os.path.exists(self.img_save_folder):
            cv2.imwrite(save_path, resimg)
        else:
            os.makedirs(self.img_save_folder)
            cv2.imwrite(save_path, resimg)
        print("******Classification result of single image saved :"+save_path+"******")
        return self.img_save_folder,self.single_img_file_name,save_path
    
    def classifyvideo(self):
        video_path = self.video_folder+'/'+self.video_name # .../*.mp4
        # 视频存储路径
        save_path = self.video_save_folder + "/"+self.video_name
        if not os.path.exists(self.video_save_folder):  
            os.makedirs(self.video_save_folder)  
        input_video = cv2.VideoCapture(video_path)
        # 获取视频帧率和大小  
        fps = int(input_video.get(cv2.CAP_PROP_FPS))
        width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # 定义编码器并创建VideoWriter对象  
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 选择编码方式，这里是'mp4v'  
        output_video = cv2.VideoWriter(save_path, fourcc, fps, (width, height))
        # 设置整个视频处理的进度条
        total_frames = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))
        pbar = tqdm(total=total_frames, desc="Processing video", unit="frames")
        # 处理视频帧
        for _ in range(total_frames):
            # 读取某一帧
            success, frame = input_video.read()
            if success:
                # 使用yolov8进行预测
                results = self.model(frame)
                # 可视化结果
                annotated_frame = results[0].plot()
                # 将带注释的帧写入视频文件
                output_video.write(annotated_frame)
                # 更新进度条
                pbar.update(1)
            else:
                # 最后结尾中断视频帧循环
                break
        # 若有部分帧未正常打开，进度条是不会达到百分之百的，下面这行代码会让进度条跑满
        pbar.update(total_frames - pbar.n)
        # 完成视频处理，关闭进度条
        pbar.close()
        # 释放读取和写入对象
        input_video.release()
        output_video.release()
        print("******Classification result of video saved :"+save_path+"******")
        return self.video_save_folder,self.video_name,save_path
'''
# 使用示例  
img_folder = 'YOLOclassifier_data/images'  
single_img_file_name = 'cardboard1.jpg'     
video_folder = 'YOLOclassifier_data/videos'
video_name = 'download1.mp4'
model_path = 'best.pt'
# 现在传递所有必要的参数  
yolo = YoloClassifier(img_folder, single_img_file_name, video_folder, video_name, model_path)
yolo.classifyOneImg()
#yolo.classifyvideo()'''
