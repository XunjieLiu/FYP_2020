import cv2
import numpy as np
import os
from Utils import get_blank, ero_dila
from Image_Entropy import get_entropy
import math


def get_diff(origin, new_img):
    blank = get_blank(origin)

    blank[abs(origin - new_img) <= 10] = 0

    return cv2.subtract(new_img, origin)


path = "E:\\Study\\2019-Summer\\SURF\\CNN\\images\\60%2387V0.51um2.2mm"  # 文件夹目录
images = []

with os.scandir(path) as entries:
    for entry in entries:
        with os.scandir((os.path.join(path, entry.name))) as new_list:
            if entry.name == "overall" or entry.name == "all":
                break

            for e in new_list:
                current = os.path.join(path, entry.name)
                img = cv2.imread(os.path.join(current, e.name), 0)
                # img = ero_dila(img, 5)
                images.append(img)

                break

diff1 = get_diff(images[0], images[1])
diff2 = get_diff(images[1], images[2])

cv2.imshow("Diff1", diff1)
cv2.imshow("Diff2", diff2)
cv2.waitKey(0)
# print(get_entropy(diff1))
# print(get_entropy(diff2))
# print(get_entropy(images[1]))
# print(get_entropy(images[0]))
