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
from tensorflow.keras.models import load_model



path = 'myData'
testRatio = 0.2
valRatio = 0.2
imagesDimensions = (32, 32, 3)

batchSizeVal = 50
epochsVal = 1
stepperEpoch = 2000

count = 0
images = []
classNo = []
myList = os.listdir(path)
print("Total no of classes detected :",len(myList))
noOfClasses = len(myList)
print("Importing classes......")

for x in range(0, noOfClasses):
    myPicList = os.listdir(path + "/" + str(count))
    #print(myPicList)
    for y in myPicList:
        curImg = cv2.imread(path + "/" + str(count) + "/" + y)
        curImg = cv2.resize(curImg, (imagesDimensions[0], imagesDimensions[1]))
        images.append(curImg)
        classNo.append(count)
    print(count, end= " ")
    count +=1
print(" ")
print("Total no of images in image list = ",len(images))
print("Total IDS in classNo list = ", len(classNo))


images = np.array(images)
classNo = np.array(classNo)



print(images.shape)
print(classNo.shape)

# Splitting data
x_train, x_test, y_train, y_test = train_test_split(images, classNo, test_size= testRatio)
x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, test_size= valRatio)



print("Data Shapes")
print("Train", end= "");print(x_train.shape, y_train.shape)
print("Validation", end= "");print(x_validation.shape, y_validation.shape)
print("Test", end= "");print(x_test.shape, y_test.shape)
assert(x_train.shape[0] == y_train.shape[0]), "The no of images in not equal to the no of label in training set"
assert(x_validation.shape[0] == y_validation.shape[0]), " The no of images is not equal to the number of label in validation set "
assert(x_test.shape[0] == y_test.shape[0]), "The number of images in not equal to the number of labels in test set"
assert(x_train.shape[1:]==(imagesDimensions)), "The dimension of the training images are wrong"
assert(x_validation.shape[1:] == (imagesDimensions)), "The dimension of the validation images are wrong"
assert(x_test.shape[1:] == (imagesDimensions)), "The dimension of the test images are wrong"

print(x_train.shape)
print(x_test.shape)
print(x_validation.shape)

noOfSamples = []
for x in range(0, noOfClasses):
    #print(len(np.where(y_train == x)[0]))
    noOfSamples.append(len(np.where(y_train == x)[0]))
print(noOfSamples)

plt.figure(figsize= (10, 5))
plt.bar(range(0, noOfClasses), noOfSamples)
plt.title("No of images of each classes")
plt.xlabel("Class ID")
plt.ylabel("No of images")
plt.show()



def preProcessig(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img/255
    return img

#img = preProcessig(x_train)
#img = cv2.resize(img,(300,300))
#cv2.imshow("gd", img)
#cv2.waitKey(0)
x_train = np.array(list(map(preProcessig, x_train)))
x_test = np.array(list(map(preProcessig, x_test)))
x_validation = np.array(list(map(preProcessig, x_validation)))






print(x_train.shape)
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)
x_validation = x_validation.reshape(x_validation.shape[0], x_validation.shape[1], x_validation.shape[2], 1)

print("==================================================================================")
print(x_train.shape)
print(x_test.shape)
print(x_validation.shape)


dataGen = ImageDataGenerator(width_shift_range=0.1,
                             height_shift_range=0.1,
                             zoom_range=0.2,
                             shear_range=0.1,
                             rotation_range=10)

dataGen.fit(x_train)
y_train = to_categorical(y_train, noOfClasses)
y_test = to_categorical(y_test, noOfClasses)
y_validation = to_categorical(y_validation, noOfClasses)


def myModel():
    noOfFilters = 60
    sizeOfFilter1 = (5, 5)
    sizeOfFilter2 = (3, 3)
    sizeOfPool = (2, 2)
    noOfNode = 500

    model = Sequential()
    model.add((Conv2D(noOfFilters, sizeOfFilter1, input_shape=(imagesDimensions[0], imagesDimensions[1], 1),activation='relu')))

    model.add((Conv2D(noOfFilters, sizeOfFilter1, activation='relu')))
    model.add(MaxPooling2D(pool_size=sizeOfPool))
    model.add((Conv2D(noOfFilters//2, sizeOfFilter2, activation='relu')))
    model.add((Conv2D(noOfFilters//2, sizeOfFilter2, activation='relu')))
    model.add(MaxPooling2D(pool_size=sizeOfPool))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(noOfNode, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(noOfClasses, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])
    return model


model = myModel()

print(model.summary())

history = model.fit(dataGen.flow(x_train,y_train,
                                 batch_size=batchSizeVal),
                                steps_per_epoch=stepperEpoch,
                                epochs=epochsVal,
                                validation_data=(x_validation,y_validation),
                                shuffle=1)


score = model.evaluate(x_test, y_test,verbose=0)
print("Test score = ", score[0])
print("Test accuracy =", score[1])


# saving and loading the .h5 model

# save model
model.save('gfgModel.h5')
print('Model Saved!')

# load model
savedModel = load_model('gfgModel.h5')
savedModel.summary()





