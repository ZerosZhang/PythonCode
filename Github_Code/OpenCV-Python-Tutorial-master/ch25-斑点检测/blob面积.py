import cv2
from matplotlib import pyplot as plt


def imshow(img, name="default"):
    temp = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(5, 5))
    plt.title(name, fontsize='xx-large')
    plt.imshow(temp)


"""
寻找轮廓是针对白色物体的，一定要保证物体是白色，而背景是黑色，不然很多人在寻找轮廓时会找到图片最外面的一个框。
"""

img = cv2.imread("blob.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换为灰度图
# _, dst = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)  # 这里只需要使用简单二值化就行
dst = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 101, 100)  # 大津二值化
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))  # 形态学去噪
dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, element)  # 开运算去噪

# 检测轮廓
contours, hierarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 5)  # 绘制轮廓

count = 0  # 米粒总数
ares_avrg = 0  # 米粒平均
# 遍历找到的所有米粒
for cont in contours:

    ares = cv2.contourArea(cont)  # 计算包围性状的面积

    if ares < 50:  # 过滤面积小于10的形状
        continue
    count += 1  # 总体计数加1
    ares_avrg += ares

    print("{}-blob:{}".format(count, ares), end="  ")  # 打印出每个米粒的面积

    rect = cv2.boundingRect(cont)  # 提取矩形坐标

    print("x:{} y:{}".format(rect[0], rect[1]))  # 打印坐标

    cv2.rectangle(img, rect, (0, 255, 0), 3)  # 绘制矩形

    y = 10 if rect[1] < 10 else rect[1]  # 防止编号到图片之外

    cv2.putText(img, str(count), (rect[0], y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1)  # 在米粒左上角写上编号

print(f"米粒平均面积:{round(ares_avrg / ares, 2)}")  # 打印出每个米粒的面积

cv2.namedWindow("src", 1)  # 创建一个窗口
cv2.imshow('src', img)  # 显示原始图片

cv2.waitKey(0)
