import cv2
import numpy as np

"""
https://www.wolai.com/zeros/f1xjK569Pn2TeHTJSdiJmF?theme=light
"""

img = cv2.imread('image\Lenna.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, None, fx=0.8, fy=0.8)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)  # 将图像转换到np.uint8
cv2.putText(laplacian, "laplacian", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 2)
"""#########################################################################################"""
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)  # 将图像转换到np.uint8
cv2.putText(sobel_x, "sobel_x", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 2)

sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)
cv2.putText(sobel_y, "sobel_y", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 2)

sobel_xy = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
cv2.putText(sobel_xy, "sobel_xy", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 2)

# 不建议直接计算
# sobel_xy = cv2.Sobel(img, cv2.CV_32F, 1, 1, ksize=3)
# sobel_xy = cv2.convertScaleAbs(sobel_xy)
"""#########################################################################################"""
scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharr_x = cv2.convertScaleAbs(scharr_x)  # 将图像转换到np.uint8
cv2.putText(scharr_x, "scharr_x", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 2)

scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharr_y = cv2.convertScaleAbs(scharr_y)
cv2.putText(scharr_y, "scharr_y", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 2)

scharr_xy = cv2.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)
cv2.putText(scharr_xy, "scharr_xy", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 2)

# 该函数用于数组的拼接，0表示纵向，1表示横向，hstack和vstack有同样的效果
complement = np.ones(img.shape[::-1], np.uint8) * 255  # 与原图一样大的纯白填充图,这里不指定uint8会显示异常
white_column_split = np.ones((img.shape[0], 1), np.uint8) * 255  # 1列的白色分隔符
result_1 = np.concatenate((img, white_column_split, sobel_x, white_column_split, sobel_y), axis=1)
cv2.imshow('result_1', result_1)
cv2.waitKey(0)
result_2 = np.concatenate((img, white_column_split, scharr_x, white_column_split, scharr_y), axis=1)
cv2.imshow('result_2', result_2)
cv2.waitKey(0)
result_3 = np.concatenate((sobel_xy, white_column_split, scharr_xy, white_column_split, laplacian), axis=1)
cv2.imshow('result_3', result_3)
cv2.waitKey(0)

cv2.destroyAllWindows()
