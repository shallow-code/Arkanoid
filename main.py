import pyglet
import sources.global_variables as globvars
from sources.game_board import *


#creo la finestra di gioco
game_window = pyglet.window.Window(globvars.board_W, globvars.board_H)

#creo il background
background_sprite = pyglet.sprite.Sprite(globvars.background_image, batch=globvars.main_batch, group=globvars.background)

#Creo la griglia (mattoncini) di gioco: si inzia dal livello 1; poi si dovrà riaggiornarlo
grid_lvl1=SetGrid("utils\\Rosettas\\Level1.csv")


@game_window.event

def on_draw():
	game_window.clear()
	globvars.main_batch.draw()


if __name__ == '__main__': 
	pyglet.app.run()