import pyglet
import csv
import numpy as np 
import sources.global_variables as globvars



#classe generica (basata sugli sprite) che definisce i blocchi
#TO DO: inserire animazioni blocco 3 e capsule 

# 1 -> blocco vita 2
# 2 -> blocco colorato
# 3 -> blocco che si rigenera
# 4 -> blocco immortale


class Brick(pyglet.sprite.Sprite):
    def __init__(self, btype,*args, **kwargs):
        super(Brick,self).__init__(img=globvars.bricks_im[btype], *args, **kwargs)

        self.life=1

        if btype=="4":
        	self.life=9999

        if btype=="1":
        	self.life=2






# classe che crea il muro di blocchi
# la griglia è 27x13 blocchi

class SetGrid:
	def __init__(self,path_to_rosetta):

		self.shape=[globvars.grid_W,globvars.grid_H]

		self.grid=np.empty(shape=self.shape,dtype=object)
		self.bricks=np.empty(shape=self.shape,dtype=object)

		#leggo file di costruzione da utils
		with open(path_to_rosetta) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for i,row in enumerate(csv_reader):
				for j,col in enumerate(row):

					self.grid[i,j]=col
					btype=col

					#converto in coordinate pixel
					board_y=globvars.board_H-i*globvars.brick_H
					board_x=j*globvars.brick_W

					#creo il mattoncino
					if btype!="0":
						self.bricks[i,j]=Brick(x=board_x ,y=board_y ,batch = globvars.main_batch, group=globvars.foreground, btype=btype)


	def print(self):
		print(self.grid)