import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

a='address of the image'
img=cv.imread(a)
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
height, width = img.shape[:2]

a=int(height/3)
b=int(width/3)
h1=[0,a,2*a,height]
w1=[0,b,2*b,width]
print(a,b)

m=[]   #images
c=[]   #coordinates for bounding boxes
#1X1
for i in range(3):
    for j in range(3):
        m.append(img[i*a:(i*a+a),j*b:(j*b+b)])        
        c.append([(i*a,j*b),(i*a+a,j*b+b)])
           
#2X2
for i in range(2):
    for j in range(2):
        m.append(img[i*a:(i*a+2*a),j*b:(j*b+2*b)])
        c.append([(i*a,j*b),(i*a+2*a,j*b+2*b)])

#3X3
for i in range(1):
    for j in range(1):
        m.append(img[i*a:(i*a+3*a),j*b:(j*b+3*b)])
        c.append([(i*a,j*b),(i*a+3*a,j*b+3*b)])
#1X2
for i in range(3):
    for j in range(2):
        m.append(img[i*a:(i*a+a),j*b:(j*b+2*b)])
        c.append([(i*a,j*b),(i*a+a,j*b+2*b)])
#1X3
for i in range(3):
     for j in range(1):
         m.append(img[i*a:(i*a+a),j*b:(j*b+3*b)])
         c.append([(i*a,j*b),(i*a+a,j*b+3*b)])
#2X1
for i in range(2):
    for j in range(3):
        m.append(img[i*a:(i*a+2*a),j*b:(j*b+1*b)])
        c.append([(i*a,j*b),(i*a+2*a,j*b+b)])
#2X3
for i in range(2):
    for j in range(1):
        m.append(img[i*a:(i*a+2*a),j*b:(j*b+3*b)])
        c.append([(i*a,j*b),(i*a+2*a,j*b+3*b)])
       
#3X1
for i in range(1):
    for j in range(3):
        m.append(img[i*a:(i*a+3*a),j*b:(j*b+1*b)])
        c.append([(i*a,j*b),(i*a+3*a,j*b+b)])
#3X2
for i in range(1):
    for j in range(2):
        m.append(img[i*a:(i*a+3*a),j*b:(j*b+2*b)])
        c.append([(i*a,j*b),(i*a+3*a,j*b+2*b)])

total_images=len(m)
points_length=len(c)
