import os
import configparser
import getopt
import sys

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
    model_path = config_handler['models']['model_path']
    ip_address = config_handler['external']['ip']
    debug_mode = config_handler.getboolean('setting', 'debug_mode')
    return ip, port, upload_folder,download_folder,model_path,ip_address,debug_mode

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