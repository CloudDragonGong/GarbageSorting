import cv2
from ultralytics import YOLO
import os
class YoloClassifier():
    def __init__(self,img_folder, single_img_file_name, video_folder, video_name, model_path):
        # 传入：图片文件夹，单个图片名称，视频文件夹，视频文件名称，加载模型，结果文件夹，均为根目录下路径（root/)
        # 生成：结果文件夹data_savefold 含/images与/videos 分别存放图片和视频检测结果 结果名称与源文件相同
        # 流程：1.传入参数 
        # 2.显示图片/视频检测结果在窗口 
        # 3.若无结果文件夹则生成 将结果保存至结果文件夹中
        # 4.返回结果文件夹 文件名 总路径 eg:data_savefold/images/cardboard1.jpg
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
        # 显示图片，不需要可注释
        cv2.imshow("yolo", resimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # 图片存储路径
        save_path = self.img_save_folder + "/"+self.single_img_file_name
        if os.path.exists(self.img_save_folder):
            cv2.imwrite(save_path, resimg)
        else:
            os.makedirs(self.img_save_folder)
            cv2.imwrite(save_path, resimg)

        print("******Result saved :"+save_path+"******")
        return self.img_save_folder,self.single_img_file_name,save_path
    
    def classifyvideo(self):
        video_path = self.video_folder+'/'+self.video_name# .../*.mp4
        input_video = cv2.VideoCapture(video_path)
        # 获取视频帧率和大小  
        fps = int(input_video.get(cv2.CAP_PROP_FPS))
        width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # 视频存储路径
        save_path = self.video_save_folder + "/"+self.video_name
        if not os.path.exists(self.video_save_folder):  
            os.makedirs(self.video_save_folder)  
        # 定义编码器并创建VideoWriter对象  
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 选择编码方式，这里是'mp4v'  
        output_video = cv2.VideoWriter(save_path, fourcc, fps, (width, height))
        while True:  
            ret, frame = input_video.read()
            if not ret:  
                break  # 读取完成  
            res = self.model.predict(source = frame,save=False)
            res1 = res[0]
            resvideo = res1.plot()
            # 显示视频帧
            cv2.imshow('yolo',resvideo)
            # 写入处理后的帧到输出视频  
            output_video.write(resvideo)   
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        input_video.release()  
        cv2.destroyAllWindows()

        print("******Result saved :"+save_path+"******")
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
#yolo.classifyOneImg()
yolo.classifyvideo()'''
