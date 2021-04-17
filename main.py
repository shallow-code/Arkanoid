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
SetGrid("utils\\Rosettas\\Test.csv")

#Creo la navicella
vault=Player(x=globvars.board_W/2 ,y=25 ,batch = globvars.main_batch, group=globvars.foreground, vault_state="0")

#Creo pallina
pallina=Pallina(x=globvars.board_W/2 ,y=40 ,batch = globvars.main_batch, group=globvars.foreground)



def resuscita_blocco(delay,x,y):
	brick=Brick(x=x ,y=y,batch = globvars.main_batch, group=globvars.foreground, btype="3",redivivo=True)
	brick.life=1
	globvars.alive_bricks.append(brick)


#update positions
def update(dt):


	vault.update(dt)
	pallina.update(dt)


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
	for brick in globvars.alive_bricks:


		# la pallina si trova dentro il mattoncino
		if (pallina.x  <= brick.x + brick.width/2 and pallina.x >= brick.x - brick.width/2) \
		and(pallina.y  <= brick.y+brick.height/2 and pallina.y  >= brick.y-brick.height/2):


			case=-1

			if not (pallina.last_x <= brick.x + brick.width/2 and pallina.last_x >= brick.x - brick.width/2):
				pallina.V_x*=-1

			if not (pallina.last_y <= brick.y + brick.height/2 and pallina.last_y >= brick.y - brick.height/2):
				pallina.V_y*=-1

			brick.life-=1
			collided_bricks.append(brick)

		if brick.life==0:
			brick.isdead=True
	
	for brick in collided_bricks:
		if not brick.isdead:
			globvars.flashes.append(Flash(x=brick.x ,y=brick.y, batch = globvars.main_batch, group=globvars.forestrings))
	

	for f in globvars.flashes:
		if f.isdead:
			f.delete()
			globvars.flashes.remove(f)

	for brick in globvars.alive_bricks:
		if brick.isdead:

			x=brick.x
			y=brick.y

			brick.delete()
			globvars.alive_bricks.remove(brick)

			if brick.btype=="3":
				pyglet.clock.schedule_once(resuscita_blocco, delay=10,x=x,y=y) 

			

#event handlers
game_window.push_handlers(vault.key_handler)
game_window.push_handlers(pallina.key_handler)

@game_window.event
def on_draw():
	game_window.clear()
	globvars.main_batch.draw()

if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1/200.0) 
	pyglet.app.run()