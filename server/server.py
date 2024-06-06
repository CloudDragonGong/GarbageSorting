import os

import const
import main
from main import *
from flask import send_file, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import utils
from main import app, ALLOWED_EXTENSIONS
from model.YOLO_classifier import YoloClassifier
from server import response
import service

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.post('/img_upload/single')
def SingleImgUpload():
    """
    single img upload
    """
    if 'img' not in request.files:
        app.logger.error("The image format is incorrect")
        return response.response(500, "The image format is incorrect")
    file = request.files['img']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config[UPLOAD_FOLDER], filename))
        return response.response(200, "ok",filename)
    return response.response(500, "Incorrect imgs format")




@app.get('/img_classify/single')
def SingleImgClassify():
    """
    单个图片上传，调度model
    :return: 标注好的图片
    """
    if 'filename' not in request.args:
        app.logger.error("request args is incorrect")
        return response.response(500, "request args is incorrect")
    filename = request.args['filename']
    if len(filename) == 0:
        return response.response(500, "filename is incorrect")
    elif utils.check_file_in_folder(app.config[UPLOAD_FOLDER], filename):
        worker = service.ImgWorker(app.config[UPLOAD_FOLDER],main.yolo)
        res_filename =worker.get_img_res(os.path.join(app.config[UPLOAD_FOLDER], filename))
        if res_filename is const.SINGLE_IMG_ERROR:
            return response.response(500, const.SINGLE_IMG_ERROR)
        if res_filename is not None and os.path.exists(os.path.join(app.config[DOWNLOAD_FOLDER], res_filename)):
            reply = {
                "image_url" : "/img_download/" + res_filename,
            }
            return response.response(200, "ok",response.serialize(reply))
        else:
            return response.response(500, const.SINGLE_IMG_ERROR)

@app.route('/img_download/<filename>')
def SingleImgDownload(filename):
    image_path = os.path.join(app.config[DOWNLOAD_FOLDER],filename)
    if not os.path.exists(image_path):
        return response.response(500, const.SINGLE_IMG_NOT_FOUND)
    return send_file(image_path,mimetype='image/jpg')

def response_test():
    return jsonify("ok")


@app.post("/img_upload_test")
def SingleImgSave():
    if 'imgs' not in request.files:
        app.logger.error("The image format is incorrect")
        return response.response(500, "The image format is incorrect")
    file = request.files['imgs']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['IMAGE_POSITION'], filename))
        return response.response(200, "ok")
    return response.response(500, "Incorrect imgs format")
