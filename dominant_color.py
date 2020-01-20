#doinant color without k means
import heapq as hq
import numpy as np 
import matplotlib.pyplot as plt 
import cv2 

a='image.jpeg'
img=cv2.imread(a)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
h,w,c=img.shape
z=img.reshape((-1,1))
z=np.float32(z)
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
k=3
ret,label1,center1=cv2.kmeans(z,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
center1=np.uint8(center1)
res1=center1[label1.flatten()]
img=res1.reshape((img.shape))
img=cv2.resize(img,(100,100))
img=cv2.resize(img,(100,100))
r=[]
b=[]
g=[]
for l in img:
    for p in l:
        tr,tb,tg=p
        r.append(tr)
        b.append(tb)
        g.append(tg)

r=np.array(r)
g=np.array(g)
b=np.array(b)
m=list(zip(r,g,b))
n=list(set(m))

f=[]
for i in range(0,len(n)):
    f.append(m.count(n[i]))

k=f
k.sort(reverse=True)
c=0
for i in range(0,len(k)):
    if(k[i]>50):
       c=c+1
    else:
       break
z=[] #Dominant colors      
for i in range(0,c):
    z.append(n[f.index(k[i])])

print(z)   
          
         
