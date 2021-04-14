import pyglet
import sources.global_variables as globvars
from sources.game_board import *
from sources.vault import *

#creo la finestra di gioco
game_window = pyglet.window.Window(globvars.board_W, globvars.board_H)

#creo il background
background_sprite = pyglet.sprite.Sprite(globvars.background_image, batch=globvars.main_batch, group=globvars.background)

#Creo la griglia (mattoncini) di gioco: si inzia dal livello 1; poi si dovrà riaggiornarlo
bricks=SetGrid("utils\\Rosettas\\Level1.csv")

#Creo la navicella
vault=Player(x=globvars.board_W//2 ,y=25 ,batch = globvars.main_batch, group=globvars.foreground, vault_state="0")


#update positions
def update(dt):
    vault.update(dt)

#event handlers
game_window.push_handlers(vault.key_handler)


@game_window.event
def on_draw():
	game_window.clear()
	globvars.main_batch.draw()

if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1/60.0) 
	pyglet.app.run()