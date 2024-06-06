import getopt
import os
import sys
from flask import Flask
from flask_cors import CORS
from flask import send_file, flash, request, redirect, url_for, jsonify
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
# config
UPLOAD_FOLDER = 'E:\myrepository\GarbageSorting\imgs'
IP = "127.0.0.1"
PORT = 5000
CONFIG_FILE = 'config.json'

app = Flask(__name__)
CORS(app)
app.config[IMAGE_POSITION] = UPLOAD_FOLDER


from server.server import *

def read_argv():
    config_path = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:", ["help", "config="])
    except getopt.GetoptError as err:
        print("main.py -c <config file path>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("main.py -c <config file path>")
            sys.exit()
        elif opt in ("-c", "--config"):
            config_path = arg
    return config_path


if __name__ == '__main__':
    app.config[IP_ADDRESS], app.config[PORT], app.config[UPLOAD_FOLDER] ,app.config[DOWNLOAD_FOLDER]= conf.read_config(read_argv())
    app.run(host=app.config[IP_ADDRESS], port=app.config[PORT], debug=True)
