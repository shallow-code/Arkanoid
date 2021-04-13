import cv2
import numpy as np
import matplotlib.pyplot as plt 
import sys


thispath=sys.path[0]

class Brick:
	def __init__(self,gridX,gridY,btype,color=""):

		def color_texture(color):

			brick=np.zeros(shape=(self.height,self.width,3),dtype=np.uint8)

			colors={}
			colors["R"]=[200,0,0]
			colors["A"]=[100,100,200]
			colors["B"]=[0,0,200]
			colors["Y"]=[255,255,100]

			


			texture = np.array([\
				[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],\
				[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0],\
				[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0],\
				[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0],\
				[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0],\
				[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],dtype=np.uint8)


			mycolor=colors[color]
			mylight_color=[min(255,x+150) for x in mycolor]

			ColBrick=brick[:]
			ColBrick[texture==1]=mycolor
			ColBrick[texture==2]=mylight_color


			return ColBrick



		
		self.gridXY=(gridX,gridY)
		self.width=17
		self.height=7
		self.X=self.width*gridX
		self.Y=self.height*gridY
		self.ColBrick=np.zeros(shape=(self.height,self.width,3),dtype=np.uint8)
		self.life=1
		self.type=btype


		if btype=="1":

			img=cv2.imread(thispath+"\\utils\\Bricks\\Type1.png")
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			self.ColBrick=img
			self.life=2
			
		if btype=="2":
			self.ColBrick=color_texture(color)


		if btype=="3":			
			img=cv2.imread(thispath+"\\utils\\Bricks\\Type3.png")
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			self.ColBrick=img

		if btype=="4":			
			img=cv2.imread(thispath+"\\utils\\Bricks\\Type4.png")
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			self.ColBrick=img	
			self.life=9999		


	def print_properties(self):
		print("")
		print("Larghezza (Pixel):",self.width)
		print("Altezza (Pixel):",self.height)
		print("Tipo Mattone:",self.type)
		print("Vita Mattone:",self.life)
		print("Posizione In Griglia:",self.gridXY)
		print("Posizione In Immagine:","("+str(self.X)+","+str(self.Y)+")")