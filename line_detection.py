import cv2
import numpy as np
import matplotlib.pyplot as plt 

img8=cv2.VideoCapture('video.mp4')
while True:
      ret, img=img8.read() 
      if not ret:
         img8=cv2.VideoCapture('/home/ananya/Documents/ananya/manas/harder_challenge_video.mp4')
         continue                                                                                       
      image=img
      image1=img
      img7=np.zeros_like(img)
      img10=np.zeros_like(image)
      img=cv2.GaussianBlur(img,(5,5),50)
      h,b=img.shape[:2]
      img2=np.zeros_like(image)
      img4=np.zeros_like(image1)
      img5=img4
      img6=img
      img=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
      img=cv2.rectangle(img,(b,700),(0,h),(0,0,0),-1)
      pt1=np.array([[[0,0],[b,0],[b,h],[995,h],[540,450],[450,450],[180,h],[0,h]]],dtype=np.int32)
      img=cv2.drawContours(img,pt1,0,(0,0,0),-1)
      yl=np.array([0,94,140])
      yu=np.array([48,255,255])
      m1=cv2.inRange(img,yl,yu)
      m1=cv2.cvtColor(m1,cv2.COLOR_GRAY2RGB)
      img=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
      wl=np.array([0,0,205])
      wu=np.array([255,50,255])
      m2=cv2.inRange(img,wl,wu)
      m2=cv2.rectangle(m2,(0,h),(b,653),(0,0,0),-1)
      m2=cv2.rectangle(m2,(0,0),(b,500),(0,0,0),-1)
      m2=cv2.rectangle(m2,(0,467),(745,653),(0,0,0),-1)
      pt1=np.array([[[b,653],[b,457],[745,457],[1006,653]]],dtype=np.int32)
      m2=cv2.drawContours(m2,pt1,0,(0,0,0),-1)
      white=[255]
      d=np.where(m1==white)
      d1=np.where(m2==white)
      coordinate=zip(d[0],d[1])
      coordinate1=zip(d1[0],d1[1])
      n=len(coordinate)
      n1=len(coordinate1)
      if n>0:
         m,c=np.polyfit(d[1],d[0],1)
         img7=np.zeros_like(image)
         if m>-0.25:
            m=mp
            c=cp
         y1=h
         x1=(y1-c)/m
         x1=x1.round(0)
         x1=int(x1)
         y2=480
         x2=(y2-c)/m
         x2=x2.round(0)
         x2=int(x2)  
         img7=cv2.line(img7,(x1,y1),(x2,y2),(255,255,255),15) 
         mp=m
         cp=c
      if n1>0:
          m1,c1=np.polyfit(d1[1],d1[0],1)
          img10=np.zeros_like(image1)
        
          y3=h
          x3=(y3-c1)/m1
          x3=x3.round(0)
          x3=int(x3)
          y4=480l
          x4=(y4-c1)/m1
          x4=x4.round(0)
          x4=int(x4)
          mp1=m1
          cp1=c1
          g=[m1]
          n3=len(g)
          if n1>7000:
             img4=np.zeros_like(image)
          elif n1<150:
             img4=np.zeros_like(image)
          else:
             img4=cv2.line(img4,(x3,y3),(x4,y4),(255,255,255),15)
          if m1<0.40:
             img4=np.zeros_like(image) 
          if c1<-400:
             img4=np.zeros_like(image) 
             
      else:
          img4=np.zeros_like(image)
      if n>0:
         if n1>0:
            img11=cv2.add(img7,img4)
      elif n>0:
           if n1==0:
              img11=img4
      elif n==0:
           if n1>0:
              img11=img7
      else:
          img11=np.zeros_like(image)
      img12=cv2.add(img11,image)
      if m>-0.45:
         print("d")
      if m<-0.70:
         print("a")
      
      cv2.imshow('hey',	img12)
      
      key=cv2.waitKey(27)
      if key == 27:
         break
img.release()
cv2.destroyAllWindows()
