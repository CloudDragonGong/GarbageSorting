from abc import ABCMeta, abstractmethod

class YoloClassifier():
    def __init__(self,img_folder, single_img_file_name):
        self.single_img_file_name = single_img_file_name
        self.img_folder = img_folder
        self.model = YOLO(model_path)

    def classifiyOneImg(self):
        """
        根据single_img_file_name,img_folder路径的图片识别
        :return:save后的filename,save的file也放在 img_folder 中
        """
        img_path = os.path.join(self.img_folder, self.single_img_file_name)  
        if not os.path.isfile(img_path):  
            raise FileNotFoundError(f"File {self.single_img_file_name} not found.")  
        results = self.model.predict(img_path,save=True)
        """通过修改ultralytics/settings.yaml配置文件更改保存路径
        以下通过代码控制
        from ultralytics.utils import SETTINGS
        update_params = {'runs_dir': img_folder}
        SETTINGS.update(update_params)
        """
        return single_img_file_name
        pass
