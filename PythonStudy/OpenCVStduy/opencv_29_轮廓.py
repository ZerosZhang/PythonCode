import cv2

"""
https://www.wolai.com/zeros/2jMDYKdTYEcCoYCq6cwzv5?theme=light
轮廓和边缘的区别：
轮廓是连续的，而边缘是断断续续的。
"""

img_rgb = cv2.imread('image/pic_0012.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

ret, img_bin = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 第三个参数表示要画的轮廓的下标，设为-1表示全画
contours_index = -1
draw_img = img_rgb.copy()
cv2.drawContours(draw_img, contours, contours_index, (0, 0, 255), 1)

for index, _ in enumerate(contours):
    print(f"{index + 1}:本轮廓的关键点个数为：{len(_)}")
print(f"共{len(contours)}条轮廓")

cv2.putText(draw_img, f"contours({contours_index})", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
cv2.imshow('contours', draw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cnt = contours[0]
print(f"轮廓面积：{cv2.contourArea(cnt)}")
print(f"轮廓周长：{cv2.arcLength(cnt, True)}")

# 轮廓近似
cnt = contours[1]
epsilon = 0.01 * cv2.arcLength(cnt, True)  # 该值越小，轮廓越精细
approx = cv2.approxPolyDP(cnt, epsilon, True)
draw_img = img_rgb.copy()
res = cv2.drawContours(draw_img, [approx], -1, (0, 0, 255), 2)

# 外接矩阵
x, y, w, h = cv2.boundingRect(cnt)
rect = cv2.rectangle(draw_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

contours_area = cv2.contourArea(cnt)
rect_area = w * h
extent = contours_area / rect_area
print(f"轮廓面积与外接矩形比：{extent}")

# 外接圆
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
circle = cv2.circle(draw_img, center, radius, (255, 0, 0), 2)

cv2.putText(draw_img, f"approx", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
cv2.imshow('approx', draw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
