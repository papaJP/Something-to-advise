#coding: utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cell.jpg' ,1)

r = cv2.split(img)
col = 2

if len(img.shape) == 3:
	height, width, channels = img.shape[:3]
	print(3)
else:
	height, width = img.shape[:2]
	channels = 1
	print(1)

#print(int(img.dtype))


myzeros = np.zeros((r[col].shape[0],r[col].shape[1]),img.dtype)

#np.savetxt('C:/Users/Administrator/myp/ML/RCG/test.csv',r[2],fmt="%s",delimiter=',')


#my_img = cv2.merge((r,g,b))

for i in range(r[col].shape[0]):
	for j in range(r[col].shape[1]):
		if r[col][i][j] > 100:
			r[col][i][j] = 255
		else:
			r[col][i][j] = 0 

#img = cv2.merge((r[2],myzeros,myzeros))

distmap = cv2.distanceTransform(r[2],cv2.DIST_L2,5)

out = distmap*0
ksize=10

for x in range(ksize,distmap.shape[0]-ksize*2):
    for y in range(ksize,distmap.shape[1]-ksize*2):
        if distmap[x,y]>0 and distmap[x,y]==np.max(distmap[x-ksize:x+ksize,y-ksize:y+ksize]):
            out[x,y]=1
            
out = cv2.dilate(out,(3,3))

#contours, _ = cv2.findContours(out.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours, _ = cv2.findContours(r[2].astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

arr=[]


for i in contours:
    x_=0
    y_=0
    for j in i:
        x_ += j[0][0]
        y_ += j[0][1]
    arr.append([x_/len(i), y_/len(i)])
arr = np.array(arr)

img = cv2.merge((r[2],r[1],r[0]))

for i in range(0, len(contours)):
    if len(contours[i]) > 0:

        # remove small objects
        #if cv2.contourArea(contours[i]) < 500:
        #   continue

        cv2.polylines(img, contours[i], True, (255, 255, 255), 1)








#my_img = cv2.merge((distmap,myzeros,myzeros))

#my_img = cv2.merge((r[2],r[1],r[0]))
#plt.imshow(img[0:100,0:100])
plt.imshow(img)

print(len(arr))
#
plt.colorbar()
plt.show()
np.savetxt('C:/Users/Administrator/myp/ML/RCG/test.csv',r[2],fmt="%s",delimiter=',')
