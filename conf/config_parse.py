import os
import configparser

def read_config(config_path):
    if not os.path.exists(config_path):
        print("config not found")
        raise FileNotFoundError
    config_handler = configparser.ConfigParser()
    config_handler.read(config_path)
    ip = config_handler['machine']['ip']
    port = config_handler['machine']['port']
    upload_folder = config_handler['img_path']['upload_folder']
    download_folder = config_handler['img_path']['download_folder']
    return ip, port, upload_folder,download_folder
