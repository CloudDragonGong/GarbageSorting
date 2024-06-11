from flask import Flask, send_file, abort
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = r'../uploads'
app.config['demo upload path'] = UPLOAD_FOLDER


@app.route('/get_image')
def get_image():
    image_path = os.path.join(app.config['demo upload path'], 'QQ20211113-0.JPG')

    if not os.path.exists(image_path):
        abort(404)

    return send_file(image_path, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)