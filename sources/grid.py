import numpy as np
import csv
from sources.bricks import *
import cv2

# la griglia è 27x13 blocchi

# 1 -> blocco vita 2
# 2 -> blocco colorato
# 3 -> blocco che si rigenera
# 4 -> blocco immortale

class Grid:
	def __init__(self,path_to_rosetta):

		self.shape=[27,13]
		self.grid=np.empty(shape=self.shape,dtype=object)


		#leggo file di costruzione
		with open(path_to_rosetta) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for i,row in enumerate(csv_reader):
				for j,col in enumerate(row):
					self.grid[i,j]=col

	def print(self):
		print(self.grid)






class Tabellone:
	def __init__(self,grid,sfondo):
		#traduco da griglia di stringhe a griglia di bricks

		width=17
		height=7

		self.immagine=np.zeros(shape=(27*height,13*width,3),dtype=np.uint8)
		self.GridBricks=np.empty(shape=(27,13),dtype=object)

		#creo sfondo immagine
		#print(sfondo)
		bkgrnd=cv2.imread(sfondo)
		bkgrnd = cv2.cvtColor(bkgrnd, cv2.COLOR_BGR2RGB)

		bkgrH,bkgrW=bkgrnd.shape[:2]
		stepW=self.immagine.shape[1]//bkgrW
		stepH=self.immagine.shape[0]//bkgrH


		for ix in range(stepW+1):
			for iy in range(stepH+1):

				W=self.immagine.shape[1]-ix*bkgrW
				H=self.immagine.shape[0]-iy*bkgrH

				if ix<stepW and iy<stepH:
					self.immagine[iy*bkgrH:(iy+1)*bkgrH,ix*bkgrW:(ix+1)*bkgrW]=bkgrnd

				elif ix==stepW and iy<stepH:
					self.immagine[iy*bkgrH:(iy+1)*bkgrH,ix*bkgrW:]=bkgrnd[:,:W]

				elif ix<stepW and iy==stepH:
					self.immagine[iy*bkgrH:,ix*bkgrW:(ix+1)*bkgrW]=bkgrnd[:H,:]

				elif ix==stepW and iy==stepH:					
					self.immagine[iy*bkgrH:,ix*bkgrW:]=bkgrnd[:H,:W]



		gridshape=grid.shape

		for y in range(gridshape[0]):
			for x in range(gridshape[1]):

				color=""
				element=grid.grid[y,x]
				btype=element[0]
				mybrick=""

				if btype!="0":

					if len(element)==2:
						color=element[1]

					mybrick=Brick(x,y,btype,color)
					self.immagine[y*height:(y+1)*height,x*width:(x+1)*width,:]=mybrick.ColBrick
					
				
				self.GridBricks[y,x]=mybrick


	def Resize(self,scalex,scaley):

		img_H,img_W=self.immagine.shape[:2]
		H,W=self.GridBricks.shape[:2]

		imgdim=(img_W*scalex,img_H*scaley)

		self.immagine=cv2.resize(self.immagine,imgdim,interpolation=cv2.INTER_NEAREST)

		for y in range(H):
			for x in range(W):
				if self.GridBricks[y,x]!="":
					self.GridBricks[y,x].Y*=scaley
					self.GridBricks[y,x].X*=scalex
					self.GridBricks[y,x].width*=scalex
					self.GridBricks[y,x].height*=scaley
					self.GridBricks[y,x].ColBrick=cv2.resize(self.GridBricks[y,x].ColBrick,(self.GridBricks[y,x].width,self.GridBricks[y,x].height),interpolation=cv2.INTER_NEAREST)




