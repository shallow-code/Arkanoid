import cv2
import numpy as np 
import matplotlib.pyplot as plt

width=17
hight=7
brick=np.zeros(shape=(hight,width,3),dtype=np.uint8)


texture_1 = np.array([\
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],\
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0],\
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0],\
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0],\
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0],\
	[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],dtype=np.uint8)



color=[200,0,0]
color_bright=[min(255,x+150) for x in color]




brick_col=brick[:]
brick_col[texture_1==1]=color
brick_col[texture_1==2]=color_bright
# i contorni neri


plt.imshow(brick_col)
plt.show()