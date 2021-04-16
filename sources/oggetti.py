import pyglet
import sources.global_variables as globvars
from pyglet.window import key
import math



#player
class Player(pyglet.sprite.Sprite):
    def __init__(self, vault_state, *args, **kwargs):
        super().__init__(img=globvars.vault_anim_states[vault_state], *args, **kwargs)

        self.isdead = False
        self.state= vault_state

        self.key_handler = key.KeyStateHandler()
        self.V_x = globvars.speed_platform
        

    def update(self,dt):
        if self.key_handler[key.LEFT]:
            self.x -= self.V_x * dt
            if self.x < globvars.vault_W//2:
                self.x=globvars.vault_W//2

        if self.key_handler[key.RIGHT]:
            self.x += self.V_x * dt
            if self.x > globvars.board_W - globvars.vault_W//2:
                self.x=globvars.board_W - globvars.vault_W//2


    def get_ball_new_angle(self, hit_position):
        pi=3.14159265358979
        return ( - 0.5*(hit_position) * (pi) / self.width)



class Pallina(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(img=globvars.pallina_im, *args, **kwargs)

        self.isdead = False
        self.isMoving=False

        self.key_handler = key.KeyStateHandler()

        self.V=globvars.speed_ball
        self.V_x = globvars.speed_platform
        self.V_y=0

        self.last_x=self.x
        self.last_y=self.y

        self.nw=(self.x-self.width/2,self.y+self.height/2)
        self.ne=(self.x+self.width/2,self.y+self.height/2)
        self.sw=(self.x-self.width/2,self.y-self.height/2)
        self.se=(self.x+self.width/2,self.y-self.height/2)

    def get_distance(self,point):
        return math.sqrt((math.pow(self.x-point[0],2)+math.pow(self.y-point[1],2)))


    def update(self,dt):

        self.last_x=self.x
        self.last_y=self.y

        #se la pallina non si muove ancora, segue la navicella
        if not self.isMoving:
            if self.key_handler[key.LEFT]:
                self.x -= self.V_x * dt
                if self.x < globvars.vault_W//2:
                    self.x=globvars.vault_W//2

            if self.key_handler[key.RIGHT]:
                self.x += self.V_x * dt
                if self.x > globvars.board_W - globvars.vault_W//2:
                    self.x=globvars.board_W - globvars.vault_W//2

            #la pallina inizia a muoversi
            if self.key_handler[key.UP]:           

                self.isMoving=True
                self.V_x=0
                self.V_y=globvars.speed_ball

        else:
            #faccio attenzione ai bordi del gioco        
            self.y +=  self.V_y * dt
            self.x +=  self.V_x * dt

            if self.y >= globvars.board_H:
                self.V_y*=-1
                self.y = globvars.board_H

            if self.x >= globvars.board_W: 
                self.V_x*=-1
                self.x=globvars.board_W


            if self.x <= 0:
                self.V_x*=-1
                self.x=0



class Flash(pyglet.sprite.Sprite):
    def __init__(self,*args, **kwargs):
        super(Flash,self).__init__(img=globvars.bricks_im["2W"], *args, **kwargs)

        self.isdead=False
        pyglet.clock.schedule_interval(self.die, 1/10.) 
        

    def die(self,dt):
        self.isdead=True