import cv2
import numpy as np

img_rgb = cv2.imread('image/Mario/mario.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
print(f"原图像大小:{img_gray.shape}")
template = cv2.imread('image/Mario/mario_coin.png', 0)
print(f"模板图像大小:{template.shape}")
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
print(f"结果大小:{res.shape}")

# 计算大于阈值的点的个数
threshold = 0.8
loc = np.where(res >= threshold)
count = 0
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    count += 1
print(count)

cv2.putText(img_rgb, f"match", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
cv2.imshow('match', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
