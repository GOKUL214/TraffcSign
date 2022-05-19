import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.python import tf2


imgOrginal = cv2.imread("Test/02708.png")


#load model
model = load_model('gfgModel.h5')

def preProcessig(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img/255
    return img



img = np.asarray(imgOrginal)
img = cv2.resize(img,(32,32))
img = preProcessig(img)
cv2.imshow("Preprossed image", img)
img = img.reshape(1, 32, 32, 1)

#predict
prediction = model.predict(img)
#print(prediction)
classIndex = np.argmax(prediction, axis=1)
print("Class no is :", classIndex)









