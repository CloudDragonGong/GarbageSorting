from abc import ABCMeta, abstractmethod


class YoloClassifier():
    def __init__(self,img_folder, single_img_file_name):
        self.single_img_file_name = single_img_file_name
        self.img_folder = img_folder
        self.client = None # 识别器

    def classfiyOneImg(self):
        """
        根据single_img_file_name,img_folder路径的图片识别
        :return:save后的filename,save的file也放在 img_folder 中
        """
        pass
