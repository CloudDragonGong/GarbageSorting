import os

import const
import main
from main import *
from flask import send_file, flash, request, redirect, url_for, jsonify, render_template
from werkzeug.utils import secure_filename
import utils
from main import app, ALLOWED_EXTENSIONS
from model.YOLO_classifier import YoloClassifier
from server import response
import service


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 上传图片并分类
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
        filename = utils.generate_unique_file_name(secure_filename(file.filename))
        input_path = os.path.join(app.config[UPLOAD_FOLDER], filename)
        file.save(input_path)
        worker = service.ImgWorker(app.config[UPLOAD_FOLDER], main.yolo)
        res_filename, type = worker.get_img_res(img_path=input_path)
        if res_filename is const.SINGLE_IMG_ERROR:
            app.logger.error(res_filename)
            return response.response(500, const.SINGLE_IMG_ERROR)
        if res_filename is not None and os.path.exists(os.path.join(app.config[DOWNLOAD_FOLDER], res_filename)):
            reply = {
                "image_url": "/img_download/" + res_filename,
                "type": type,
            }
            return response.response(200, "ok", reply)
        else:
            app.logger.error(res_filename)
            return response.response(500, const.SINGLE_IMG_ERROR)
    app.logger.error("file is not allowed or none")
    return response.response(500, "file is not allowed or none")

# 下载图片
@app.route('/img_download/<filename>')
def SingleImgDownload(filename):
    image_path = os.path.join(app.config[DOWNLOAD_FOLDER], filename)
    if not os.path.exists(image_path):
        return response.response(500, const.SINGLE_IMG_NOT_FOUND)
    return send_file(image_path, mimetype='image/jpg')

def response_test():
    return jsonify("ok")

# demo测试接口（生产环境不用）
@app.route("/demo")
def Html():
    return app.send_static_file("demo2.html")

# 返回模版
@app.route("/sort")
def Sort():
    # return app.send_static_file("pictureDivision.html")
    server_url = request.args.get('server_url', 'http://'+app.config[IP_INTERNAL]+":"+app.config[PORT])
    return render_template("pictureDivision.html", server_url=server_url)



# 测试使用（生产环境不用）
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
