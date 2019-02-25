import os
from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file (filename):
    return '.' in filename and \
       filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    white = 0
    black = 0

    if allowed_file(file.filename):
        file.save(f)
        myimage = Image.open(f)

        for i in range (0 , myimage.size[0]):
            for j in range (0 , myimage.size[1]):
                if myimage.getpixel((i, j))  == (255, 255, 255):
                    white += 1
                if myimage.getpixel((i, j)) == (0, 0, 0):
                    black += 1







        if black > white:
            return "black"

        if black < white:
            return "white"

        if  black == 0 and white == 0:
            return "none"

        if black == white and black != 0:
            return "equal"




if __name__=='__main__':
    app.run(port=4990, debug=True)