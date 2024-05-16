import os
from app import app, ALLOWED_EXTENSIONS
from flask import send_file, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from model.YOLO_classifier import YoloClassifier
from response import response


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.post('/imgclassify/single')
def SingleImgClassify():
    """
    单个图片上传，调度model
    :return: 标注好的图片
    """
    if 'imgs' not in request.files:
        app.logger.error("The image format is incorrect")
        return response(500, "The image format is incorrect")
    file = request.files['imgs']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        app.logger.error("file name is none ")
        return response(500, "file name is none ")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['IMAGE_POSITION'], filename))
        try:
            classifier = YoloClassifier(app.config['IMAGE_POSITION'], filename)
            path = classifier.classfiyOneImg()
            return send_file(path_or_file=path)
        except:
            return response(500,"classifier.classfiyOneImg() error")

    return response(500,"Incorrect imgs format")
