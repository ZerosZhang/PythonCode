#!/usr/bin/python

# Standard imports
import cv2
import numpy as np
from matplotlib import pyplot as plt


def imshow(name, img):
    temp = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(6, 6))
    plt.title(name, fontsize='xx-large')
    plt.imshow(temp)
    plt.show()


# Read image
im = cv2.imread("img_1.bmp", cv2.IMREAD_GRAYSCALE)
iret, im = cv2.threshold(im, 50, 255, cv2.THRESH_BINARY)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 15
params.maxThreshold = 50

# Filter by Area.
params.filterByArea = True
params.minArea = 1000
params.maxArea = 20000

# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)
print(f"找到了{len(keypoints)}个点")
count = 0
for _blob in keypoints:
    count += 1
    print(f"{count}:斑点的面积是{_blob.size}")

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
imshow("Keypoints", im_with_keypoints)
