import cv2

"""
https://www.wolai.com/zeros/wuVHFUN2PHiFf9nb49gJGM?theme=light
"""
img = cv2.imread('image/pic_0012.jpg', cv2.IMREAD_GRAYSCALE)

# 高斯金字塔
lower_reso = cv2.pyrDown(img)
height_reso = cv2.pyrUp(img)
cv2.imshow('img', img)
cv2.imshow('lower_reso', lower_reso)
cv2.imshow('height_reso', height_reso)
cv2.waitKey(0)

# 拉普拉斯金字塔
down = cv2.pyrDown(img)
up_down = cv2.pyrUp(down)
img_laplacian = img - up_down
cv2.imshow('img_laplacian', img_laplacian)
cv2.waitKey(0)

cv2.destroyAllWindows()
