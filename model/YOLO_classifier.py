from abc import ABCMeta, abstractmethod


class YoloClassifier():
    def __init__(self,img_folder, single_img_file_name):
        self.single_img_file_name = single_img_file_name
        self.img_folder = img_folder

    def classfiyOneImg(self):
        pass
