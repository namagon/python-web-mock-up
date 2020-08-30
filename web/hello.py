import numpy as np
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        data = request.files['image']
        img = Image.open(data)
        img = np.array(img)
        print(img)
        name = 'Image'
        im = None
    else:
        im = None
    return render_template('hello.html', title='test', name=name, im=im)


@app.route('/image', methods=['POST'])
def image():
    name = "Image"
    return render_template('hello.html', title='test', name=name)


if __name__ == '__main__':
    app.run(debug=True)
