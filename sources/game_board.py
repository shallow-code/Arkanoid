import pyglet
import csv
import sources.global_variables as globvars



#classe generica (basata sugli sprite) che definisce i blocchi
#TO DO: inserire animazioni blocco 3 e capsule 

# 1 -> blocco vita 2
# 2 -> blocco colorato
# 3 -> blocco che si rigenera
# 4 -> blocco immortale


class Brick(pyglet.sprite.Sprite):
    def __init__(self, btype,grid_X,grid_Y,*args, **kwargs):
        super(Brick,self).__init__(img=globvars.bricks_im[btype], *args, **kwargs)

        self.life=1
        self.grid_X=grid_X
        self.grid_Y=grid_Y
        self.btype=btype
        self.isdead=False

        if btype=="4":
        	self.life=9999

        if btype=="1":
        	self.life=2


# classe che crea il muro di blocchi
# la griglia è 27x13 blocchi

def SetGrid(path_to_rosetta):


	bricks=[]

	#leggo file di costruzione da utils
	with open(path_to_rosetta) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for i,row in enumerate(csv_reader):
			for j,col in enumerate(row):

				btype=col

				#converto in coordinate pixel
				board_y=globvars.board_H-i*globvars.brick_H-globvars.brick_H//2
				board_x=j*globvars.brick_W+globvars.brick_W//2

				#creo il mattoncino
				if btype!="0":
					brick=Brick(x=board_x ,y=board_y,batch = globvars.main_batch, group=globvars.foreground, btype=btype, grid_X=j, grid_Y=i)
					bricks.append(brick)

	return bricks


