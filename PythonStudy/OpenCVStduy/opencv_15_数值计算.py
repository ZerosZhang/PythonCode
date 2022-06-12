import cv2
import numpy as np

# 图像数值计算
x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x, y))  # 对应像素相加之后，超过255的等于255
print(x + y)  # 对应像素值相加之后 % 256，2的8次方等于256
print(cv2.addWeighted(x, 0.2, y, 0.8, 0))  # 0.2 * x + 0.8 * y + 0

"""
推荐使用cv.add()
"""

# 图像融合
# y = ax + (1-a)x

img1 = cv2.imread('image/pic_0005.jpg')
img1 = cv2.resize(img1, (500, 300))

img2 = cv2.imread('image/pic_0007.jpg')
img2 = cv2.resize(img2, (500, 300))

dst = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 按位运算

"""
cv.bitwise_not
cv.bitwise_and
cv.bitwise_or
cv.bitwise_xor
"""
# 可以用来提取图像
