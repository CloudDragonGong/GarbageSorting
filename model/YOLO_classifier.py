import os
import cv2
from tqdm import tqdm
from ultralytics import YOLO


class YoloClassifier():
    def __init__(self, model_path, img_out_folder, video_out_folder):
        self.img_out_folder = img_out_folder
        self.video_out_folder = video_out_folder
        self.model = YOLO(model_path)

    def classify_one_img(self, img_path, img_out_filename):
        if not os.path.isfile(img_path):
            raise FileNotFoundError(f"File {img_path} not found.")

        img = cv2.imread(img_path)
        res = self.model.predict(source=img, save=False)
        resimg = res[0].plot()
        # todo: get type kevin 快写
        type = ""
        save_path = os.path.join(self.img_out_folder, img_out_filename)

        # 图片存储路径
        if os.path.exists(self.img_out_folder):
            cv2.imwrite(save_path, resimg)
        else:
            os.makedirs(self.img_out_folder)
            cv2.imwrite(save_path, resimg)
        print("******Classification result of single image saved :" + save_path + "******")
        return save_path, type

    def classify_video(self,video_path,video_out_filename):
        save_path = os.path.join(self.video_out_folder, video_out_filename)
        if not os.path.exists(self.video_out_folder):
            os.makedirs(self.video_out_folder)
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
        type_list = []
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
        print("******Classification result of video saved :" + str(save_path) + "******")
        return save_path, type_list


if __name__ == "__main__":
    yolo = YoloClassifier("../models/best.pt", "../imgs", "")
    path,type = yolo.classify_one_img("../imgs/78969a6a22595394a95641b66ea7b38e.jpg", "78969a6a22595394a95641b66ea7b38e_out.jpg")
    print(path,type)
