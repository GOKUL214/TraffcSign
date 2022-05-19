import numpy as np
import cv2
import os

from keras.optimizer_v1 import Adam
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers import Dropout, Flatten
from keras.layers import Dense
from tensorflow.python import tf2
import pickle
from tensorflow.keras.models import load_model

path = 'Test'
testRatio = 0.2
valRatio = 0.2
imagesDimensions = (32, 32, 3)

curImg = cv2.imread("Test/00000.png")
# cv2.imshow("gd", curImg)
curImg = cv2.resize(curImg, (imagesDimensions[0], imagesDimensions[1]))

curImg = np.array(curImg)

def preProcessig(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img/255
    return img

x_test = np.array(preProcessig(curImg))

x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)

print(x_test.shape)
