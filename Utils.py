import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import copy


def mean(x):
    return sum(x) / len(x)


def get_contours(img):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图处理
    ret, thresh = cv2.threshold(img, 100, 255, 0)  # 二值化处理，参数需要调整
    '''
    cv2.findContours(image, mode, method[, contours[, hierarchy[, offset ]]])

    第一个参数是寻找轮廓的图像；

    第二个参数表示轮廓的检索模式，有四种（本文介绍的都是新的cv2接口）：
        cv2.RETR_EXTERNAL表示只检测外轮廓
        cv2.RETR_LIST检测的轮廓不建立等级关系
        cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
        cv2.RETR_TREE建立一个等级树结构的轮廓。

    第三个参数method为轮廓的近似办法
        cv2.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
        cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
        cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似算法
    '''

    binary, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_NONE)
    '''
    返回值：
    (OpenCV 3版本会返回3个值)

    1. Binary: 不知道
    2. Contours：Numpy列表，存着所有的contours，需要用循环读取所有的contour
    3. Hierarchy：轮廓的层次结构，基本不用
    '''

    return contours


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


# 统计概率霍夫线变换
def line_detect_possible_demo(image):
    blank = np.zeros((image.shape[0], image.shape[1]))
    blank[blank < 1] = 255
    edges = cv2.Canny(image, 50, 150, apertureSize=3)  # apertureSize参数默认其实就是3
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 60, minLineLength=30, maxLineGap=100)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(blank, (x1, y1), (x2, y2), (0, 255, 0), 1)

    cv2.imshow("line_detect_possible_demo", blank)


def convexHull(contours, img):
    # 图像凸包的处理过程
    for i in range(1, len(contours)):
        cnt = contours[i]
        hull = cv2.convexHull(cnt, returnPoints=False)
        defects = cv2.convexityDefects(cnt, hull)

        if defects is None:
            continue
        else:
            for j in range(defects.shape[0]):
                s, e, f, d = defects[j, 0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                cv2.line(img, start, end, [0, 255, 0], 5)

    return img


# 删除面积过小的轮廓
def contour_filter(contours):
    new_contours = []

    for c in contours:
        if cv2.contourArea(c) > 100:
            new_contours.append(c)

    return new_contours


# 获取逼近轮廓
def approx(contours):
    approx_con = []
    for c in contours:
        approx_con.append(cv2.approxPolyDP(c, 5, True))

    return approx_con


# 获取空白画布
def get_blank(img):
    blank = np.zeros((img.shape[0], img.shape[1]))
    blank[blank < 1] = 255

    return blank


# get slop value of two points
def get_slope(point1, point2):
    if point1.x == point2.x:
        return math.inf
    else:

        return format((point1.y - point2.y) / (point1.x - point2.x), '.1f')


def draw_line(blank, point1, point2):
    x1 = point1.x
    x2 = point2.x
    y1 = point1.y
    y2 = point1.y
    cv2.line(blank, (int(x1), int(y1)), (int(x2), int(y2)), (0, 100, 100))

    return blank


def get_max_area(contours):
    max = 0

    for c in contours:
        if cv2.contourArea(c) > max:
            max = cv2.contourArea(c)

    return max


def draw_line(img, length, thickness):
    green = (0, 255, 0)  # BGR
    red = (0, 0, 255)
    white = (255, 255, 255)

    color = white
    cv2.line(img, (480, 450), (length + 480, 450), color, thickness)

    font = cv2.FONT_HERSHEY_SIMPLEX  # 使用默认字体
    cv2.putText(img, '0.1mm', (465, 440), font, 0.8, color,
                1)  # 添加文字，1.2表示字体大小，（0,40）是初始的位置，(255,255,255)表示颜色，2表示粗细

def unevenLightCompensate(img, blockSize):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    average = np.mean(gray)

    rows_new = int(np.ceil(gray.shape[0] / blockSize))
    cols_new = int(np.ceil(gray.shape[1] / blockSize))

    blockImage = np.zeros((rows_new, cols_new), dtype=np.float32)
    for r in range(rows_new):
        for c in range(cols_new):
            rowmin = r * blockSize
            rowmax = (r + 1) * blockSize
            if (rowmax > gray.shape[0]):
                rowmax = gray.shape[0]
            colmin = c * blockSize
            colmax = (c + 1) * blockSize
            if (colmax > gray.shape[1]):
                colmax = gray.shape[1]

            imageROI = gray[rowmin:rowmax, colmin:colmax]
            temaver = np.mean(imageROI)
            blockImage[r, c] = temaver

    blockImage = blockImage - average
    blockImage2 = cv2.resize(blockImage, (gray.shape[1], gray.shape[0]), interpolation=cv2.INTER_CUBIC)
    gray2 = gray.astype(np.float32)
    dst = gray2 - blockImage2
    dst = dst.astype(np.uint8)
    dst = cv2.GaussianBlur(dst, (3, 3), 0)
    dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

    return dst

if __name__ == '__main__':
    # Reading the input image
    # img = cv2.imread('E:\\Study\\2019-Summer\\SURF\\CNN\\data\\images\\20190808\\0808172539.jpg', 0)
    # img = cv2.imread('E:\\Study\\2019-Summer\\SURF\\CNN\\data\\images\\Scaffold\\0730103043.jpg', 0)
    # img = cv2.imread('E:\\Study\\2019-Summer\\SURF\\CNN\\data\\images\\20190808\\0808170829.jpg', 0)

    img = cv2.imread(r'E:\Study\Year 4\FYP\images\dataset_scaffold\Bad\161746.jpg')
    # img = cv2.imread('E:\\Study\\2019-Summer\\SURF\\CNN\\dataset_scaffold\\Bad\\153834.jpg')

    origin = copy.deepcopy(img)

    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # 获取灰度图

    thresh2 = ero_dila(thresh2, 2)  # 边缘平滑处理

    contours = contour_filter(get_contours(thresh2))  # 获取轮廓（过大或者过小的轮廓去除）
    print(len(contours))
    draw_line(img, 35, 5)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 5)

    cv2.imshow("Origin", origin)
    cv2.imshow("Img", img)
    # cv2.imshow("Bin", thresh2)

    cv2.waitKey(0)
