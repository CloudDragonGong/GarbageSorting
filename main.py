import os
from flask import Flask
from flask_cors import CORS
from flask import send_file, flash, request, redirect, url_for, jsonify
from server import response
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'E:\myrepository\GarbageSorting\imgs'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
CORS(app)
app.config['IMAGE_POSITION'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.post("/img_upload_test")
def SingleImgSave():
    if 'imgs' not in request.files:
        app.logger.error("The image format is incorrect")
        return response(500, "The image format is incorrect")
    file = request.files['imgs']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['IMAGE_POSITION'], filename))
        return response(200, "ok")


from server.server import *

if __name__ == '__main__':
    app.run(debug=True)
