import os.path

import const
import utils
from model import YoloClassifier
from const import *


class ImgWorker():
    def __init__(self, img_output_folder_path, worker: YoloClassifier):
        self.img_output_folder_path = img_output_folder_path
        self.worker = worker

    def get_img_res(self, img_path: str) -> (str, str):
        try:
            type = "test"
            output_filename = utils.generate_unique_file_name("output.png")
            # self.worker.classfiyOneImg(img_path,str(os.path.join(self.img_output_folder_path,output_filename)))
            utils.mutation(r"./uploads",output_filename)
            if output_filename is None:
                return const.FILE_NOT_FOUND, None
            return output_filename, type
        except Exception as e:
            return str(e), None
