import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


# Model Loading and dependencies

import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.python import tf2

# load model
model = load_model('gfgModel.h5')


def preProcessig(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255
    return img


UPLOAD_FOLDER = 'Uploaded'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    classIndex = 100
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            imgOrginal = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = np.asarray(imgOrginal)
            img = cv2.resize(img, (32, 32))
            img = preProcessig(img)
            img = img.reshape(1, 32, 32, 1)

            # predict
            prediction = model.predict(img)
            # print(prediction)
            classIndex = int(np.argmax(prediction, axis=1))
            print("===========================================")
            print(type(classIndex))

    if classIndex == 0:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Speed limit 20 km/hr </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 1:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Speed limit 30 km/hr </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 2:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Speed limit 50 km/hr </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 3:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Speed limit 60 km/hr </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 4:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Speed limit 70 km/hr </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 5:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Speed limit 80 km/hr </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 6:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>End of speed limit (80km/hr) </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 7:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Speed limit (100km/hr) </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 8:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Speed limit (120km/hr) </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 9:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>No passing </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 10:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>No passing veh over 3.5 tons </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 11:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Right-of-way at intersection </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 12:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Priority Road</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 13:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Yield</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 14:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Yield</h1>
    <title>Stop</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 15:
        return '''   
       <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>No vechicles</h1>
    <title>Stop</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 16:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>veh > 3.5 tons prohibited </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 17:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>No entry </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 18:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>General caution </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 19:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Dangerous curve left </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 20:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Dangerous curve right </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 21:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Double curve </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 22:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Bump road </h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 23:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Slippery road</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''


    elif classIndex == 24:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Road narrows on the right</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 25:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Road work</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''

    elif classIndex == 26:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Traffic signals</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 27:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Pedestrians</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 28:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Childern crossing</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 29:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Bicycle crossing</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 30:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Beware of ice/snow</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 31:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Wild animal crossing</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 32:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>End speed + passing limit</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 33:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Turn right ahead</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 34:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Turn left ahead</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 35:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Ahead only</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 36:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Go straight or right</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 37:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Go straight or left</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 38:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Keep right</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 39:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Keep left</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 40:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>Roundabout mandatory</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 41:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>End of no passing</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''
    elif classIndex == 42:
        return '''   
        <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>


         <h1>End no passing veh > 3.5 tons</h1>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>'''


    return '''
   <!doctype html>
<head>
    <style>

        h1 {
            color: blue;
        }

        p {
            color: red;
        }
         body {
     min-height: 100%;
}

    </style>
</head>
<body style="width: 100%; height: 100%; background-image: url('https://wallpaperaccess.com/full/2111648.jpg'); height: 100%; width: 100%;  ">

    <center>

    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </center>
</body>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)