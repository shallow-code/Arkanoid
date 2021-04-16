import pyglet
import sources.global_variables as globvars
from sources.game_board import *
from sources.oggetti import *
import math

#creo la finestra di gioco
game_window = pyglet.window.Window(globvars.board_W, globvars.board_H)

#creo il background
background_sprite = pyglet.sprite.Sprite(globvars.background_image, batch=globvars.main_batch, group=globvars.background)

#Creo la griglia (mattoncini) di gioco: si inzia dal livello 1; poi si dovrà riaggiornarlo
bricks=SetGrid("utils\\Rosettas\\Test.csv")

#Creo la navicella
vault=Player(x=globvars.board_W/2 ,y=25 ,batch = globvars.main_batch, group=globvars.foreground, vault_state="0")
#globvars.board_W/2
#Creo pallina
pallina=Pallina(x=globvars.board_W/2 ,y=40 ,batch = globvars.main_batch, group=globvars.foreground)

#update positions
def update(dt):
	vault.update(dt)
	pallina.update(dt)
	flash = pyglet.sprite.Sprite(img=globvars.bricks_im["2W"] ,x=0 ,y=0, batch = globvars.main_batch, group=globvars.forestrings)


	#pallina colpisce navicella
	if (pallina.x <= vault.x+vault.width//2 and pallina.x >= vault.x-vault.width//2) \
	and (pallina.y - pallina.height//2 <= vault.y+vault.height//2):

		hit_pos=(pallina.x-vault.x)
		angle=vault.get_ball_new_angle(hit_pos)

		#print("palla/navicella",hit_pos,angle)

		pallina.V_x=-pallina.V*math.sin(angle)
		pallina.V_y=pallina.V*math.cos(angle)

		pallina.y=40
	

	collided_bricks=[]
	# controlla se pallina colpisce mattoncino
	for brick in bricks:


		# la pallina si trova dentro il mattoncino
		if (pallina.x  <= brick.x + brick.width/2 and pallina.x >= brick.x - brick.width/2) \
		and(pallina.y  <= brick.y+brick.height/2 and pallina.y  >= brick.y-brick.height/2):


			case=-1

			collided_bricks.append(brick)

			if (pallina.last_y>=brick.y+brick.height/2) and (pallina.y<brick.y+brick.height/2):
				case=0

			if (pallina.last_y<=brick.y-brick.height/2) and (pallina.y>brick.y-brick.height/2):
				case=1

			if (pallina.last_x<=brick.x-brick.width/2) and (pallina.x>brick.x-brick.width/2):
				case=2

			if (pallina.last_x>=brick.x+brick.width/2) and (pallina.x<brick.x+brick.width/2):
				case=3


			if case==-1:

				print("colpito blocco",brick.grid_X,brick.grid_Y)
				print("velocità pallina",pallina.V_x,pallina.V_y)
				print("pallina last p",pallina.last_x, pallina.last_y)
				print("pallina p",pallina.x, pallina.y)
				print("brick dx",brick.x+brick.width/2)
				print("brick sx",brick.x-brick.width/2)
				print("brick su",brick.y+brick.height/2)
				print("brick giu",brick.y-brick.height/2)
				print("case",case)
				print("\n")


			#ha colpito su
			if case==0:
				pallina.V_y*=-1
				pallina.y=brick.y + brick.height/2 

			#ha colpito down
			if case==1:
				pallina.V_y*=-1
				pallina.y=brick.y - brick.height/2 

			# ha colpito a sx 
			if case==2:
				pallina.V_x*=-1
				pallina.x=brick.x - brick.width/2 

			# ha colpito a dx
			if case==3:
				pallina.V_x*=-1
				pallina.x=brick.x + brick.width/2 

	
#	for brick in collided_bricks:
#		print(brick.x,brick.y)
#		flash = pyglet.sprite.Sprite(img=globvars.bricks_im["2W"] ,x=brick.x ,y=brick.y, batch = globvars.main_batch, group=globvars.forestrings)


#event handlers
game_window.push_handlers(vault.key_handler)
game_window.push_handlers(pallina.key_handler)

@game_window.event
def on_draw():
	game_window.clear()
	globvars.main_batch.draw()

if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1/400.0) 
	pyglet.app.run()