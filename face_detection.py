import cv2
import numpy as np
import matplotlib.pyplot as plt


im1=cv2.imread('1.jpg',0)

face_cascade=cv2.CascadeClassifier('default.xml')

face_rects=face_cascade.detectMultiScale(im1,scaleFactor=1.2,minNeighbors=5)
for (x,y,w,h) in face_rects:
        cv2.rectangle(im1,(x,y),(x+w,y+h),(255,255,255),10)
plt.imshow(result)
plt.show()



