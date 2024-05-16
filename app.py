from flask import Flask

UPLOAD_FOLDER = '/imgs'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['IMAGE_POSITION'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(debug=True)