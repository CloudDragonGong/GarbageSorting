import getopt
import os
import sys
from flask import Flask
from flask_cors import CORS
from flask import send_file, flash, request, redirect, url_for, jsonify

import model
from server import response
from werkzeug.utils import secure_filename
import conf

# global
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# const
IMAGE_POSITION = 'IMAGE_POSITION'
UPLOAD_FOLDER = 'upload_folder'
DOWNLOAD_FOLDER = 'download_folder'
IP_ADDRESS = 'IP'
PORT = "PORT"
MODLE_PATH ='model_path'
# config
UPLOAD_FOLDER = 'imgs'
IP = "127.0.0.1"
PORT = 5000
CONFIG_FILE = 'config.json'
IP_INTERNAL  = 'ip_internal'
MODE = 'mode'

# init
app = Flask(__name__)
CORS(app)
app.config[IP_ADDRESS], app.config[PORT], app.config[UPLOAD_FOLDER] ,app.config[DOWNLOAD_FOLDER] , app.config[MODLE_PATH] , app.config[IP_INTERNAL],app.config[MODE] = conf.read_config(conf.read_argv())
yolo = model.YoloClassifier(app.config[MODLE_PATH], app.config[DOWNLOAD_FOLDER], app.config[DOWNLOAD_FOLDER])

from server.server import *




if __name__ == '__main__':
    app.run(host=app.config[IP_ADDRESS], port=app.config[PORT], debug=app.config[MODE])