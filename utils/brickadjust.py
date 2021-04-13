import cv2
import matplotlib.pyplot as plt 
import numpy as np 

file="Model2.PNG"
img=cv2.imread(file)

img1=np.zeros(shape=(7,17,3),dtype=np.uint8)

img1[:-1,:-1,:]=img

#img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

cv2.imwrite("Brick3.png",img1)

