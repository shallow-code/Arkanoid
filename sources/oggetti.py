import pyglet
import sources.global_variables as globvars
from pyglet.window import key
import math



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
    def __init__(self, *args, **kwargs):
        super().__init__(img=globvars.pallina_start, *args, **kwargs)

        self.isdead = False
        self.isMoving=False
        self.state="0"

        self.key_handler = key.KeyStateHandler()

        self.V=globvars.speed_ball
        self.V_x = globvars.speed_platform
        self.V_y=0

        self.last_x=self.x
        self.last_y=self.y

        pyglet.clock.schedule_once(self.start,delay=1)

    def start(self,delay):
        self.image=globvars.pallina_im
        self.state="1"


    def get_distance(self,point):
        return math.sqrt((math.pow(self.x-point[0],2)+math.pow(self.y-point[1],2)))


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
                    self.V_x=globvars.speed_ball*math.cos(math.pi/4)
                    self.V_y=globvars.speed_ball*math.sin(math.pi/4)

            else:
                #faccio attenzione ai bordi del gioco        
                self.y +=  self.V_y * dt
                self.x +=  self.V_x * dt

                if self.y >= globvars.board_H - globvars.board_RLMargin:
                    self.V_y*=-1
                    self.y = globvars.board_H - globvars.board_RLMargin

                if self.x >= globvars.board_W - globvars.board_RLMargin: 
                    self.V_x*=-1
                    self.x=globvars.board_W - globvars.board_RLMargin


                if self.x <= globvars.board_RLMargin:
                    self.V_x*=-1
                    self.x= globvars.board_RLMargin

                if self.y<=0:
                    self.isdead=True



class Flash(pyglet.sprite.Sprite):
    def __init__(self,*args, **kwargs):
        super(Flash,self).__init__(img=globvars.bricks_im["2W"], *args, **kwargs)

        self.isdead=False
        pyglet.clock.schedule_interval(self.die, 1/10.) 
        

    def die(self,dt):
        self.isdead=True



# 1 -> blocco vita 2
# 2 -> blocco colorato
# 3 -> blocco che si rigenera
# 4 -> blocco immortale


class Brick(pyglet.sprite.Sprite):
    def __init__(self, btype,redivivo=False,*args, **kwargs):
        super(Brick,self).__init__(img=globvars.bricks_im[btype], *args, **kwargs)

        self.life=1

        self.btype=btype
        self.isdead=False
        self.redivivo=redivivo

        if btype=="4":
            self.life=-1

        if btype=="1" or (btype=="3" and not self.redivivo):
            self.life=2

        if btype=="3" and self.redivivo:
            pyglet.clock.schedule_once(self.rise_life,10)

    def rise_life(self,delay):
        self.life=2