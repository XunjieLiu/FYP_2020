import pickle, os
import tensorflow as tf
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import numpy as np
import cv2

IMG_SIZE = 480


def erode(img, ite_time):
    kernel = np.ones((5, 5), np.uint8)
    img_ero = cv2.erode(img, kernel, iterations=ite_time)

    return img_ero


def dilation(img, ite_time):
    kernel = np.ones((5, 5), np.uint8)
    img_dila = cv2.dilate(img, kernel, iterations=ite_time)

    return img_dila


def ero_dila(img, ite_time):
    img = erode(img, ite_time)

    return dilation(img, ite_time)


def handle_img(img):
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    new_array = cv2.resize(ero_dila(thresh2, 2), (IMG_SIZE, IMG_SIZE))

    return new_array / 255


def make_test_set():
    path = r'E:\Study\Year 4\FYP\images\dataset_scaffold\Good'
    test_data = []
    
    for i in os.listdir(path):
        img = cv2.imread(os.path.join(path, i), 0)
        img = handle_img(img)
        
        test_data.append(img)

    X = np.array(test_data).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    return X
        

model = load_model('my_model.h5')

X = make_test_set()


print('test after load: ', model.predict_classes(X[0:]))