from abc import ABCMeta, abstractmethod

class YoloClassifier():
    def __init__(self,model_path,img_folder,single_img_file_name,video_folder,video_name):
        self.single_img_file_name = single_img_file_name
        self.img_folder = img_folder
        self.video_name = video_name
        self.video_folder = video_folder
        self.model = YOLO(model_path)

    def classifyOneImg(self):
        """通过修改ultralytics/settings.yaml配置文件更改保存路径
        以下通过代码控制
        from ultralytics.utils import SETTINGS
        update_params = {'runs_dir': img_folder}
        SETTINGS.update(update_params)
        """
        img_path = os.path.join(self.img_folder, self.single_img_file_name)  
        if not os.path.isfile(img_path):  
            raise FileNotFoundError(f"File {self.single_img_file_name} not found.")  
        results = self.model.predict(img_path,save=True)
       
        return single_img_file_name
        pass
        
    def classify_video(self):
    
        video_path= os.path.join(self.video_folder, self.video_name)  
        if not os.path.isfile(video_path):  
            raise FileNotFoundError(f"File {self.video_name} not found.")  
        results = self.model.predict(video_path,save=True)
        return video_name
        
        pass
