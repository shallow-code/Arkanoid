import pyglet
import csv
import sources.global_variables as globvars
from sources.oggetti import *


# classe che crea il muro di blocchi
# la griglia è 27x13 blocchi

def SetGrid(path_to_rosetta):

	#leggo file di costruzione da utils
	with open(path_to_rosetta) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for i,row in enumerate(csv_reader):
			for j,col in enumerate(row):

				btype=col

				#converto in coordinate pixel
				board_y=globvars.board_H-i*globvars.brick_H-globvars.brick_H//2
				board_x=j*globvars.brick_W+globvars.brick_W//2+globvars.board_RLMargin

				#creo il mattoncino
				if btype!="0":
					brick=Brick(x=board_x ,y=board_y,batch = globvars.main_batch, group=globvars.foreground, btype=btype)
					globvars.alive_bricks.append(brick)



