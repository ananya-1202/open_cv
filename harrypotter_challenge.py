import cv2
import numpy as np
import time

video = cv2.VideoCapture(0)

#to save the background
time.sleep(1)
kernel = np.ones((3,3),np.uint8)

for i in range(60): 
     return_val, background = video.read() 
     if return_val == False : 
         continue

while(video.isOpened()):
	return_val, image = video.read()
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
	mask2 = cv2.bitwise_not(mask)

	#removing the red color 
	res1 = cv2.bitwise_and(background, background, mask = mask1) 
	res2 = cv2.bitwise_and(image, image, mask = mask2)
	final = res1 + res2 

	cv2.imshow(final)
	k = cv2.waitKey(10) 
	if k == ord('q'): 
		break  
