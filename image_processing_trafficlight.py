import cv2 
import numpy as np
import matplotlib.pyplot as plt 
a='/home/ananya/Documents/ananya/vision/traffic_sur/1.jpg'
img=cv2.imread(a)
img1=cv2.imread(a)
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 100)
img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])
mask1 = cv2.inRange(img, lower_red, upper_red)
lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])
mask2 = cv2.inRange(img,lower_red,upper_red)
mask3 = mask1+mask2
element = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
mask = cv2.erode(mask2, element, iterations = 2)
mask = cv2.dilate(mask, element, iterations = 5)
mask = cv2.erode(mask, element)
ret, thresh = cv2.threshold(mask,50,255,0)
# Find the contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# For each contour, find the convex hull and draw it
# on the original image.
for i in range(len(contours)):
    hull = cv2.convexHull(contours[i])
    cv2.drawContours(img1, [hull], -1, (255, 0, 0), 30)

plt.imshow(img1)
plt.show()
