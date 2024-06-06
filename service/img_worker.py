import const
from model import YoloClassifier
from const import *


class ImgWorker():
    def __init__(self, img_output_folder_path,worker: YoloClassifier):
        self.img_output_folder_path = img_output_folder_path
        self.worker= worker

    def get_img_res(self, img_path: str) -> str:
        try:
            filename = self.worker.classfiyOneImg(img_path, self.img_output_folder_path)
            if filename is None:
                return const.FILE_NOT_FOUND
            return filename
        except Exception as e:
            return SINGLE_IMG_ERROR
