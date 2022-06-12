import cv2
import numpy as np

"""
https://www.wolai.com/zeros/6RttqgH83Ww9WwB7S6LE93?theme=light
"""

img = cv2.imread('image/pic_0012.jpg', cv2.IMREAD_GRAYSCALE)

# 这里所用的内核为5*5的平均
blur = cv2.blur(img, (5, 5))  # 均值滤波
cv2.putText(blur, "blur", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)
# kernel = np.ones((5, 5), np.float32) / 25
# dst_1 = cv2.filter2D(img, -1, kernel)  # 均值滤波，只是使用2D卷积的函数来进行操作

# 方框滤波
boxFilter = cv2.boxFilter(img, -1, (5, 5), normalize=True)
cv2.putText(boxFilter, "box", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)
# 这里可以看normalize置为True和False各有什么效果
# boxFilter_1 = cv2.boxFilter(img, -1, (5, 5), normalize=True)
# boxFilter_2 = cv2.boxFilter(img, -1, (5, 5), normalize=False)
# cv2.putText(boxFilter_1, "normalize=True", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)
# cv2.putText(boxFilter_2, "normalize=False", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)

# 高斯滤波
gaussian = cv2.GaussianBlur(img, (5, 5), 1)
cv2.putText(gaussian, "gaussian", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)

# 中值滤波
median = cv2.medianBlur(img, 5)
cv2.putText(median, "median", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)

# 双边滤波
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.putText(bilateral, "bilateral", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)

# 该函数用于数组的拼接，0表示纵向，1表示横向，hstack和vstack有同样的效果
cv2.putText(img, "origin", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)
white_column_split = np.zeros((img.shape[0], 1), np.uint8)  # 1列的白色分隔符
result_1 = np.concatenate((img, white_column_split, blur, white_column_split, boxFilter), axis=1)
result_2 = np.concatenate((gaussian, white_column_split, median, white_column_split, bilateral), axis=1)
white_row_split = np.zeros((1, result_1.shape[1]), np.uint8)  # 1行的白色分隔符
result = np.concatenate((result_1, white_row_split, result_2), axis=0)

cv2.imshow('图像平滑对比', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
