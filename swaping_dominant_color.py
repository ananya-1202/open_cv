#swapping the dominant color 
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
img1=img
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
m=list(zip(r,b,g))
n=list(set(m))

f=[]
for i in range(0,len(n)):
    f.append(m.count(n[i]))

j=hq.nlargest(2,f)

jk=[]  
for i in range(0,len(j)):
    jk.append(n[f.index(j[i])])

#swaping the color

m1=jk[0]
m2=jk[1]
print(m1,m2)
#image[np.where((image==[0]).all(axis=1))] = [255]
#print(m1)
#print(len(np.where((img==[213,27,84]))))

print(min(f))
img1[np.where((img1 == [m1]).all(axis = 2))] = [n[f.index((min(f)))]]
img1[np.where((img1 == [m2]).all(axis = 2))] = [m1]
img1[np.where((img1 == [n[f.index((min(f)))]]).all(axis = 2))] = [m2]


plt.imshow(img1)
plt.show()
