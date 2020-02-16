import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle

DATADIR = r'E:\Study\Year 4\FYP\images\dataset_scaffold'
CATEGORIES = ['Good', 'Bad']

IMG_SIZE = 480

training_data = []


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
    
    return ero_dila(thresh2, 2)


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        clas_num = CATEGORIES.index(category)

        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), 0)
                img_array = handle_img(img_array)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))

                training_data.append([new_array, clas_num])
            except Exception as e:
                pass


create_training_data()

random.shuffle(training_data)

X = []  # features
y = []  # labels

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# save model
pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()
