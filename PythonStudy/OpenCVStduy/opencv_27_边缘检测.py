import cv2
import numpy as np

"""
https://www.wolai.com/zeros/wyBmag8C1RuPydB6X7SYPj?theme=light
"""

img = cv2.imread('image/Lenna.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, None, fx=0.8, fy=0.8)

complement = np.ones(img.shape[::-1], np.uint8) * 255  # 与原图一样大的纯白填充图,这里不指定uint8会显示异常
white_column_split = np.ones((img.shape[0], 1), np.uint8) * 255  # 1列的白色分隔符

# canny边缘检测,不同的高低阈值进行比较
edges_1 = cv2.Canny(img, 80, 150)
edges_2 = cv2.Canny(img, 200, 250)
cv2.putText(edges_1, "minVal=80, maxVal=150", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 2)
cv2.putText(edges_2, "minVal=200, maxVal=250", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 2)

# 该函数用于数组的拼接，0表示纵向，1表示横向，hstack和vstack有同样的效果
result = np.concatenate((img, white_column_split, edges_1, white_column_split, edges_2), axis=1)
cv2.imshow('canny', result)
cv2.waitKey(0)

cv2.destroyAllWindows()
