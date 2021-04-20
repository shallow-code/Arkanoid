import cv2
import glob
import matplotlib.pyplot as plt

files=glob.glob("Enemy*.png")

for f in files:
	img=cv2.imread(f,cv2.IMREAD_UNCHANGED)

#	img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

	dims=img.shape[:2]

	imgdim=(int(dims[1]*2),int(dims[0]*2))

	img=cv2.resize(img,imgdim,interpolation=cv2.INTER_NEAREST)


	cv2.imwrite("Resource\\"+f,img)