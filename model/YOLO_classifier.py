from abc import ABCMeta, abstractmethod


class YoloClassifier():
    def __init__(self):
        self.client = None # 识别器

    def classfiyOneImg(self,single_img_file_name:str, out_img_folder:str)->str:
        """
        根据single_img_file_name,img_folder路径的图片识别
        :return:save后的filename,save的file也放在 img_folder 中
        """
        pass
