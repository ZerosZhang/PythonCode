import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def imshow(name, img):
    temp = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 10))
    plt.title(name, fontsize='xx-large')
    plt.imshow(temp)
    plt.show()


def TestMain():
    img_rgb = cv2.imread(r"E:\222\Image_20210916100608848.bmp", cv2.IMREAD_COLOR)  # 这里绝对位置有误
    img_roi = img_rgb[300:3100, 500:4500]
    img_gray = cv2.cvtColor(img_roi, cv2.COLOR_RGB2GRAY)
    ret, img_bin = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY)
    params = cv2.SimpleBlobDetector_Params()

    # 表示提取白色的色块，若需要提取黑色色块可以用0
    params.blobColor = 0

    # 控制blob的区域面积大小
    params.filterByArea = True
    params.minArea = 100
    params.maxArea = 90000
    # blob的圆度限制，默认为不限制，通常不限制，除非找圆形特征
    params.filterByConvexity = True
    params.minConvexity = 0.3
    params.maxConvexity = 1.0

    params.minDistBetweenBlobs = 1  # 最小的斑点距离，不同的二值图像斑点小于该值时将被认为是同一个斑点
    params.minRepeatability = 1

    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(img_bin)
    draw_img = img_roi.copy()
    for keypoint in keypoints:
        x, y = np.int64(keypoint.pt[0]), np.int64(keypoint.pt[1])
        cv2.circle(draw_img, (x, y), 50, (0, 255, 0), 5)

    imshow("关键点", draw_img)

if __name__ == '__main__':
    TestMain()
