import pyglet
import sources.global_variables as globvars
from pyglet.window import key
import math
import random


#player
class Player(pyglet.sprite.Sprite):
    def __init__(self, vault_state="0", *args, **kwargs):
        super().__init__(img=globvars.vault_anim_states[vault_state], *args, **kwargs)

        self.isdead = False
        self.state= vault_state

        self.key_handler = key.KeyStateHandler()
        self.V_x = globvars.speed_platform

        pyglet.clock.schedule_once(self.alive_animation,1)


    def update(self,dt):

        if self.state!="0":
            if self.key_handler[key.LEFT]:
                self.x -= self.V_x * dt
                if self.x < globvars.vault_W//2 + globvars.board_RLMargin:
                    self.x=globvars.vault_W//2 + globvars.board_RLMargin

            if self.key_handler[key.RIGHT]:
                self.x += self.V_x * dt
                if self.x > globvars.board_W - globvars.vault_W//2 - globvars.board_RLMargin:
                    self.x=globvars.board_W - globvars.vault_W//2 - globvars.board_RLMargin




    def get_ball_new_angle(self, hit_position):
        pi=3.14159265358979
        return ( - 0.5*(hit_position) * (pi) / self.width)


    def alive_animation(self,delay):
        self.state="1"
        self.image=globvars.vault_anim_states["1"]




class Pallina(pyglet.sprite.Sprite):
    def __init__(self,ismoving=False,vx=globvars.speed_platform,vy=0, *args, **kwargs):
        super().__init__(img=globvars.pallina_start, *args, **kwargs)

        self.isdead = False
        self.isMoving=ismoving
        self.state="0"

        self.key_handler = key.KeyStateHandler()

        self.V=globvars.speed_ball
        self.V_x = vx
        self.V_y = vy

        self.last_x=self.x
        self.last_y=self.y

        if not self.isMoving: 
            pyglet.clock.schedule_once(self.start,delay=1)
        else:
            self.image=globvars.pallina_im
            self.state="1"

    def start(self,delay):
        self.image=globvars.pallina_im
        self.state="1"

    def get_distance(self,point):
        return math.sqrt((math.pow(self.x-point[0],2)+math.pow(self.y-point[1],2)))

    def diventaNera(self):
        self.image=globvars.pallina_nera
        self.state="2"


    def update(self,dt):

        self.last_x=self.x
        self.last_y=self.y

        #se la pallina non si muove ancora, segue la navicella
        if self.state!="0":
            if not self.isMoving:
                if self.key_handler[key.LEFT]:
                    self.x -= self.V_x * dt
                    if self.x < globvars.vault_W//2 + globvars.board_RLMargin:
                        self.x=globvars.vault_W//2 + globvars.board_RLMargin

                if self.key_handler[key.RIGHT]:
                    self.x += self.V_x * dt
                    if self.x > globvars.board_W - globvars.vault_W//2 - globvars.board_RLMargin:
                        self.x=globvars.board_W - globvars.vault_W//2 - globvars.board_RLMargin

                #la pallina inizia a muoversi
                if self.key_handler[key.UP]:           

                    self.isMoving=True
                    self.V_x=globvars.speed_ball*math.cos(math.pi/3)
                    self.V_y=globvars.speed_ball*math.sin(math.pi/3)

            else:
                #faccio attenzione ai bordi del gioco        
                self.y +=  self.V_y * dt
                self.x +=  self.V_x * dt

                if self.y >= globvars.board_H - globvars.board_RLMargin:
                    self.V_y*=-1
                    self.y = globvars.board_H - globvars.board_RLMargin
                    self.V=min(self.V+10,600)
                    globvars.speed_ball=self.V

                if self.x >= globvars.board_W - globvars.board_RLMargin: 
                    self.V_x*=-1
                    self.x=globvars.board_W - globvars.board_RLMargin
                    self.V=min(self.V+5,600)
                    globvars.speed_ball=self.V


                if self.x <= globvars.board_RLMargin:
                    self.V_x*=-1
                    self.x= globvars.board_RLMargin
                    self.V=min(self.V+5,600)
                    globvars.speed_ball=self.V

                if self.y<=0:
                    self.isdead=True



class Flash(pyglet.sprite.Sprite):
    def __init__(self,*args, **kwargs):
        super(Flash,self).__init__(img=globvars.bricks_im["2W"], *args, **kwargs)

        self.isdead=False
        pyglet.clock.schedule_interval(self.die, 1/10.) 
        

    def die(self,dt):
        self.isdead=True



class Mangione(pyglet.sprite.Sprite):
    def __init__(self,last_used,*args, **kwargs):
        super(Mangione,self).__init__(img=globvars.Mangione[0], *args, **kwargs)
        
        self.lastUsed=last_used

    def cambiaStato(self):
        if self.lastUsed:
            self.lastUsed=False
        else:
            self.lastUsed=True

    def apritiSesamo(self):
        #print("dentro")
        self.image=globvars.Mangione_anim




# 1 -> blocco vita 2
# 2 -> blocco colorato
# 3 -> blocco che si rigenera
# 4 -> blocco immortale


class Brick(pyglet.sprite.Sprite):
    def __init__(self, btype,redivivo=False,*args, **kwargs):
        super(Brick,self).__init__(img=globvars.bricks_im[btype[:2]], *args, **kwargs)

        self.life=1

        self.btype=btype
        self.isdead=False
        self.redivivo=redivivo
        self.PowerUP=None

        if len(self.btype)==3:
             self.PowerUP=self.btype[2]

        if btype=="4":
            self.life=-1

        if btype=="1" or (btype=="3" and not self.redivivo):
            self.life=2

        if btype=="3" and self.redivivo:
            pyglet.clock.schedule_once(self.rise_life,10)

    def rise_life(self,delay):
        self.life=2



class Enemy(pyglet.sprite.Sprite):
    def __init__(self,etype, *args, **kwargs):
        super().__init__(img=globvars.Enemies[etype], *args, **kwargs)
        
        self.life=1
        self.isdead=False
        self.direction=3*math.pi/2

        self.directionList=[0,math.pi,3*math.pi/2]
        self.forbiddenDirections=[]
        self.percorso=0

        self.V=globvars.speed_enemy
        self.last_x=self.x
        self.last_y=self.y
        self.deltax=0
        self.deltay=0


    def update(self,dt):

        if self.percorso>100:
            self.new_direction()
            self.percorso=0

        self.deltax=math.cos(self.direction)*self.V*dt
        self.deltay=math.sin(self.direction)*self.V*dt

        #print(deltax)
        self.last_x=self.x
        self.last_y=self.y

        self.x+=self.deltax
        self.y+=self.deltay

        self.percorso+=self.deltax+self.deltay

        if self.x<=globvars.board_RLMargin+self.width/2:
            self.direction=0

        if self.x>=globvars.board_W - globvars.board_RLMargin-self.width/2:
            self.direction=math.pi

        if self.y<=20:
            self.isdead=True

    def new_direction(self):
        copia_direzioni=self.directionList[:]

        for i in self.forbiddenDirections:
            copia_direzioni.remove(i)

        direzione_casuale=random.randint(0,len(copia_direzioni)-1)
        self.direction=copia_direzioni[direzione_casuale]





#PowerUps
class PowerUP(pyglet.sprite.Sprite):
    def __init__(self, ptype, *args, **kwargs):
        super().__init__(img=globvars.PowerUP[ptype], *args, **kwargs)

        self.ptype=ptype
        self.isdead=False

        self.V=150

    def update(self,dt):
        self.y-=self.V*dt


#stype: S,D
class Vaus_Shadow(pyglet.sprite.Sprite):
    def __init__(self, stype, refxmin, refxmax=-1, *args, **kwargs):
        super().__init__(img=globvars.VausShadows_im[stype], *args, **kwargs)

        self.key_handler = key.KeyStateHandler()
        self.stype=stype
        self.V_x=globvars.speed_platform/3
        self.refxmin=refxmin
        self.refxmax=refxmax

        if "D" in self.stype:
            self.V_x*=-1

       

    def update(self,dt):

        if not (self.key_handler[key.LEFT] or self.key_handler[key.RIGHT]):
            if "1" in self.stype:
                if abs(self.x-self.refxmin)>1 and abs(self.x-self.refxmax)<2:
                    self.x += self.V_x * dt
            elif "1" not in self.stype:
                self.x += self.V_x * dt
        
        if "D" in self.stype:
            if (self.x - self.refxmin)<0:
                self.x=self.refxmin
        if "S" in self.stype:
            if (self.x - self.refxmin)>0:
                self.x=self.refxmin            

        if self.stype=="D1":
                    
            if (self.x - self.refxmin)>64:
                self.x=self.refxmin+64

        if self.stype=="D2":
                    
            if (self.x - self.refxmin)>45:
                self.x=self.refxmin+45

        if self.stype=="S1":
            if (self.refxmin-self.x)>64:
                self.x=self.refxmin-64            

        if self.stype=="S2":
            if (self.refxmin-self.x)>45:
                self.x=self.refxmin-45 

