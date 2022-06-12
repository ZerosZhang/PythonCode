import cv2
import numpy as np

# 标定
origin_points_set = np.float32([[1698.650, 681.653],
                                [2371.946, 664.784],
                                [3049.477, 698.211],
                                [1711.106, 1327.899],
                                [2366.661, 1354.134],
                                [3034.910, 1386.819],
                                [1702.339, 1963.508],
                                [2399.918, 2010.131],
                                [3095.774, 2038.798]])

target_points_set = np.float32([[-235, 200],
                                [-255, 200],
                                [-275, 200],
                                [-235, 220],
                                [-255, 220],
                                [-275, 220],
                                [-235, 240],
                                [-255, 240],
                                [-275, 240]])
ret, inline = cv2.estimateAffine2D(origin_points_set, target_points_set, False)
print(f"使用OpenCV九点标定结果\n{ret}")

# 使用opencv转换
test_point1 = np.float32([[[1698.650, 681.653]]])
res_point1 = cv2.transform(test_point1, ret)
print(f"使用opencv：{res_point1}")

# 使用numpy转换
test_point2 = np.float32([1698.650, 681.653, 1])
res_point2 = np.dot(ret, test_point2)
print(f"使用numpy：{res_point2}")
