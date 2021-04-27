import pyglet
import sources.global_variables as globvars
from sources.game_board import *
from sources.oggetti import *
import math
import time 

player=pyglet.media.Player()
player.volume=0.2

pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')

#creo la finestra di gioco
game_window = pyglet.window.Window(globvars.board_W, globvars.board_H)


def delete_obj(delay,myobject):
	myobject.delete()


def crea_robino(delay,x,y):
	globvars.alive_enemies.append(Enemy(etype="0",x=x,y=y,batch=globvars.main_batch, group=globvars.foreground))

def apri_mangione(delay):

	x=0
	y=0

	for m in globvars.Mangioni:
		#print(m.x,m.lastUsed)
		if not m.lastUsed:
			m.apritiSesamo()
			x=m.x 
			y=m.y

	for m in globvars.Mangioni:
		m.cambiaStato()
			
	pyglet.clock.schedule_once(crea_robino,0.5,x,y)




def crea_livello():


	#creo il background
	globvars.background_sprite = pyglet.sprite.Sprite(globvars.background_image, batch=globvars.main_batch, group=globvars.background)
	
	#creo cornice
	#globvars.cornice_sprite = pyglet.sprite.Sprite(globvars.cornice_image, batch=globvars.main_batch, group=globvars.background)

	#creo mangioni
	globvars.Mangioni.append(Mangione(x=137,y=globvars.board_H-20,batch=globvars.main_batch, group=globvars.foreground,last_used=False))
	globvars.Mangioni.append(Mangione(x=451,y=globvars.board_H-20,batch=globvars.main_batch, group=globvars.foreground,last_used=True))
	
	#globvars.mangione1=pyglet.sprite.Sprite(globvars.mangione_image,x=globvars.board_W/4 ,y=globvars.board_H-12 , batch=globvars.main_batch, group=globvars.foreground)
	#globvars.mangione2=pyglet.sprite.Sprite(globvars.mangione_image,x=3*globvars.board_W/4 ,y=globvars.board_H-12 , batch=globvars.main_batch, group=globvars.foreground)



	#Creo la griglia (mattoncini) di gioco: si inzia dal livello 1; poi si dovrà riaggiornarlo
	SetGrid("utils\\Rosettas\\Level1a.csv")


	for i in range(globvars.lifes):
		globvars.l_lifes.append(pyglet.sprite.Sprite(globvars.vita_im, globvars.board_RLMargin+ 10+i*25,10, batch=globvars.main_batch, group=globvars.foreground))


	crea_giocatore()




def crea_giocatore(delay=0):
	if globvars.vault==None:
		globvars.vault=Player(x=globvars.board_W/2 ,y=25 ,batch = globvars.main_batch, group=globvars.forestrings1)

	#Creo pallina
	if len(globvars.palline)==0:
		globvars.palline.append(Pallina(x=globvars.board_W/2 ,y=42 ,batch = globvars.main_batch, group=globvars.foreground))

	#event handlers
	game_window.push_handlers(globvars.vault.key_handler)
	for pallina in globvars.palline:
		game_window.push_handlers(pallina.key_handler)

	globvars.fase_of_game ='main_game'
	


def resuscita_blocco(delay,x,y):
	brick=Brick(x=x ,y=y,batch = globvars.main_batch, group=globvars.foreground, btype="3",redivivo=True)
	brick.life=1
	globvars.alive_bricks.append(brick)


#update positions
def update(dt):

	if globvars.fase_of_game=="crea_livello":
		crea_livello()


	if 	globvars.fase_of_game =='main_game':

		if globvars.vault is None and globvars.lifes>0:
			pyglet.clock.schedule_once(crea_giocatore,1)

		#muovo la navicella
		if globvars.vault is not None:
			globvars.vault.update(dt)

			#se ombra attiva
			if "D1" in globvars.Vaus_Shadows.keys():
				globvars.Vaus_Shadows["D1"].refxmin=globvars.vault.x
				globvars.Vaus_Shadows["D2"].refxmin=globvars.Vaus_Shadows["D1"].x
				globvars.Vaus_Shadows["D1"].refxmax=globvars.Vaus_Shadows["D2"].x
				globvars.Vaus_Shadows["S1"].refxmin=globvars.vault.x
				globvars.Vaus_Shadows["S2"].refxmin=globvars.Vaus_Shadows["S1"].x
				globvars.Vaus_Shadows["S1"].refxmax=globvars.Vaus_Shadows["S2"].x

				for stype in globvars.Vaus_Shadows.keys():
					globvars.Vaus_Shadows[stype].update(dt)


		#creo robini		
		if globvars.numero_robini<3:
			globvars.numero_robini+=1
			pyglet.clock.schedule_once(apri_mangione,1+globvars.numero_robini*3.5)



		#update blocchi powerup:
		for p in globvars.alive_powerups:
			p.update(dt)

			if globvars.vault==None:
				continue

			if (p.x <= globvars.vault.x+globvars.vault.width//2 and p.x >= globvars.vault.x-globvars.vault.width//2) \
			and (p.y - p.height//2 <= globvars.vault.y+globvars.vault.height//2):

				globvars.GamePowerUpState=p.ptype
				globvars.alive_powerups.remove(p)
				p.delete()
				break

			if p.y<0:
				globvars.alive_powerups.remove(p)
				p.delete()	
				break

		# valuto l'effetto dei powerup attivi
		if globvars.GamePowerUpState:

			vaus_power_ups=["E","R","T"]


			if globvars.GamePowerUpState=="S":
				for pallina in globvars.palline:
					pallina.V=max(280,pallina.V-20)
					globvars.speed_pallina=pallina.V
				globvars.GamePowerUpState="SS"


			if globvars.GamePowerUpState=="I" and ("D1" not in globvars.Vaus_Shadows.keys()):
				globvars.Vaus_Shadows["D1"]=Vaus_Shadow(x=globvars.vault.x,y=globvars.vault.y,batch = globvars.main_batch, group=globvars.forestrings, stype="D1",refxmin=globvars.vault.x)
				globvars.Vaus_Shadows["D2"]=Vaus_Shadow(x=globvars.vault.x,y=globvars.vault.y,batch = globvars.main_batch, group=globvars.foreground, stype="D2",refxmin=globvars.vault.x)
				globvars.Vaus_Shadows["S1"]=Vaus_Shadow(x=globvars.vault.x,y=globvars.vault.y,batch = globvars.main_batch, group=globvars.forestrings, stype="S1",refxmin=globvars.vault.x)
				globvars.Vaus_Shadows["S2"]=Vaus_Shadow(x=globvars.vault.x,y=globvars.vault.y,batch = globvars.main_batch, group=globvars.foreground, stype="S2",refxmin=globvars.vault.x)


			if globvars.GamePowerUpState!="I":
				for stype in globvars.Vaus_Shadows.keys():
					globvars.Vaus_Shadows[stype].delete()
				globvars.Vaus_Shadows={}

			if globvars.GamePowerUpState=="N" and len(globvars.palline)>0 and len(globvars.palline)<3:

				x=globvars.palline[0].x
				y=globvars.palline[0].y
				vx=globvars.palline[0].V_x
				vy=globvars.palline[0].V_y

				for i in range(3-len(globvars.palline)):

					if y<20:
						continue

					globvars.palline.append(Pallina(x=x+(i+1)*10 ,y=y ,batch = globvars.main_batch, group=globvars.foreground,ismoving=True,vx=vx,vy=vy))



			if globvars.GamePowerUpState=="D" and len(globvars.palline)>0 and len(globvars.palline)<8:

				x=globvars.palline[0].x
				y=globvars.palline[0].y
				vx=globvars.palline[0].V_x
				vy=globvars.palline[0].V_y

				for i in range(8-len(globvars.palline)):

					if y<20:
						continue

					globvars.palline.append(Pallina(x=x+(i+1)*10 ,y=y ,batch = globvars.main_batch, group=globvars.foreground,ismoving=True,vx=vx,vy=vy))

				globvars.GamePowerUpState="DD"



			if globvars.GamePowerUpState=="M" and len(globvars.palline)>0:
				for pallina in globvars.palline:
					if pallina.state!="2":
						pallina.diventaNera()
						pallina.state="2"

			if globvars.GamePowerUpState in vaus_power_ups:
				if globvars.vault.state!=globvars.GamePowerUpState:
					globvars.vault.image=globvars.vault_anim_states[globvars.GamePowerUpState]
					globvars.vault.state=globvars.GamePowerUpState

			else:
				if globvars.vault.image!=globvars.vault_anim_states["1"]:
						globvars.vault.image=globvars.vault_anim_states["1"]
						globvars.vault.state="1"


		#update dei robini
		for e in globvars.alive_enemies:
			e.update(dt)
			#controllo che robino non entri in mattoncino
			for brick in globvars.alive_bricks:

				# il robino si trova dentro il mattoncino
				if (e.x-e.width/2  <= brick.x + brick.width/2 and e.x + e.width/2 >= brick.x - brick.width/2) \
				and(e.y-e.height/2  <= brick.y+brick.height/2 and e.y + e.height/2>= brick.y-brick.height/2):

					e.new_direction()
					e.x=e.last_x
					e.y=e.last_y

		for pallina in globvars.palline:
			pallina.update(dt)


			#pallina colpisce navicella
			deltaVausR=globvars.vault.x+globvars.vault.width//2
			deltaVausL=globvars.vault.x-globvars.vault.width//2

			if globvars.GamePowerUpState=="I":
				deltaVausL=min(deltaVausL,globvars.Vaus_Shadows["S2"].x-globvars.Vaus_Shadows["S2"].width//2)
				deltaVausR=max(deltaVausR,globvars.Vaus_Shadows["D2"].x+globvars.Vaus_Shadows["D2"].width//2)

			if (pallina.x <= deltaVausR and pallina.x >=deltaVausL ) \
			and (pallina.y - pallina.height//2 <= globvars.vault.y+globvars.vault.height//2):

				if globvars.vault.state=="T" and pallina.x>55+globvars.vault.x-globvars.vault.width//2 and pallina.x<70+globvars.vault.x-globvars.vault.width//2:
					continue

				hit_pos=(pallina.x-globvars.vault.x)
				if globvars.GamePowerUpState=="I":
					if pallina.x>globvars.vault.x:
						hit_pos=pallina.x-(globvars.vault.x+globvars.Vaus_Shadows["D2"].x)/2
					if pallina.x<globvars.vault.x:
						hit_pos=pallina.x-(globvars.vault.x+globvars.Vaus_Shadows["S2"].x)/2

				angle=globvars.vault.get_ball_new_angle(hit_pos)

				#print("palla/navicella",hit_pos,angle)

				pallina.V_x=-pallina.V*math.sin(angle)
				pallina.V_y=pallina.V*math.cos(angle)

				pallina.y=40
			
				player.next_source()
				player.queue(globvars.hit_sound1)
				player.play()



			# controlla se pallina colpisce mattoncino
			for brick in globvars.alive_bricks:


				# la pallina si trova dentro il mattoncino
				if (pallina.x  <= brick.x + brick.width/2 and pallina.x >= brick.x - brick.width/2) \
				and(pallina.y  <= brick.y+brick.height/2 and pallina.y  >= brick.y-brick.height/2):

					if pallina.state!="2":
						if not (pallina.last_x <= brick.x + brick.width/2 and pallina.last_x >= brick.x - brick.width/2):
							pallina.V_x*=-1

						if not (pallina.last_y <= brick.y + brick.height/2 and pallina.last_y >= brick.y - brick.height/2):
							pallina.V_y*=-1

					if pallina.state=="2":
						brick.life=0
					else:
						brick.life-=1

					if brick.life!=0:
						globvars.flashes.append(Flash(x=brick.x ,y=brick.y, batch = globvars.main_batch, group=globvars.forestrings))
						player.next_source()
						player.queue(globvars.hit_sound3)
						player.play()

				if brick.life==0:
					brick.isdead=True
					player.next_source()
					player.queue(globvars.hit_sound2)
					player.play()


			# controlla se pallina colpisce robino
			for e in globvars.alive_enemies:
				# la pallina si trova dentro il robino
				if (pallina.x  <= e.x + e.width/2 and pallina.x >= e.x - e.width/2) \
				and(pallina.y  <= e.y +e.height/2 and pallina.y  >= e.y-e.height/2):

					if not (pallina.last_x <= e.x + e.width/2 and pallina.last_x >= e.x - e.width/2):
						pallina.V_x*=-1
						e.isdead=True

					if not (pallina.last_y <= e.y + e.height/2 and pallina.last_y >= e.y - e.height/2):
						pallina.V_y*=-1
						e.isdead=True

					

	
			# rimuovo i robini morti
			for f in globvars.flashes:
				if f.isdead:
					f.delete()
					globvars.flashes.remove(f)


			# rimuovo i brick morti
			for brick in globvars.alive_bricks:
				if brick.isdead:

					x=brick.x
					y=brick.y

					if brick.btype=="3":
						pyglet.clock.schedule_once(resuscita_blocco, delay=10,x=x,y=y) 

					#rilascio il corrispondente power up
					if brick.PowerUP!=None:
						powerup=PowerUP(x=x,y=y,ptype=brick.PowerUP,batch=globvars.main_batch,group=globvars.foreground)
						globvars.alive_powerups.append(powerup)

					brick.delete()
					globvars.alive_bricks.remove(brick)



			for e in globvars.alive_enemies:
				x=e.x
				y=e.y
				if e.isdead:
					die_enemy=pyglet.sprite.Sprite(globvars.EnemyExplosion, x=x ,y=y, batch=globvars.main_batch,group=globvars.foreground)
					globvars.numero_robini-=1
					e.delete()
					globvars.alive_enemies.remove(e)
					player.next_source()
					player.queue(globvars.die_alien_sound)
					player.play()




		#controllo se pallina ancora in gioco
		for indp,pallina in enumerate(globvars.palline):
			if pallina.isdead:
				#print("pallina",indp,"morta")
				pallina.delete()
				globvars.palline.remove(pallina)

		if len(globvars.palline)==0:
			if globvars.vault is not None:
				globvars.vault.isdead=True

		#controllo se navicella ancora in gioco
		if globvars.vault is not None and globvars.vault.isdead:
			x=globvars.vault.x
			globvars.vault.delete()
			globvars.vault=None
			die_vault=pyglet.sprite.Sprite(globvars.vault_anim_states["2"], x=x ,y=25, batch=globvars.main_batch,group=globvars.foreground)
			globvars.GamePowerUpState=None

			for stype in globvars.Vaus_Shadows.keys():
				globvars.Vaus_Shadows[stype].delete()
			globvars.Vaus_Shadows={}

			player.next_source()
			player.queue(globvars.die_sound)
			player.play()

			if globvars.lifes>0:
				globvars.lifes-=1
				last_life=globvars.l_lifes[-1]
				last_life.delete()
				globvars.l_lifes.remove(last_life)


			


@game_window.event
def on_draw():
	game_window.clear()
	globvars.main_batch.draw()

if __name__ == '__main__':


	pyglet.clock.schedule_interval(update, 1/100.0) 
	pyglet.app.run()