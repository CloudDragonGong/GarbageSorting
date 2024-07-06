import os.path

import const
import utils
from model import YoloClassifier
from const import *

# worker类，调度模型处理图片分类 视频分类任务
class ImgWorker():
    def __init__(self, img_output_folder_path, worker: YoloClassifier):
        self.img_output_folder_path = img_output_folder_path
        self.worker = worker

    def get_img_res(self, img_path) -> (str,dict):
        try:
            output_filename = utils.generate_unique_file_name("output.png")
            _, type_map = self.worker.classify_one_img(img_path, output_filename)
            if output_filename is None:
                return const.FILE_NOT_FOUND, None
            return output_filename,type_map
        except Exception as e:
            return str(e), None
