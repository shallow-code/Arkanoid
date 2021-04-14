import pyglet
import sources.global_variables as globvars

#player
class Player(pyglet.sprite.Sprite):
    def __init__(self,*args, **kwargs):
        super(Player,self).__init__(img=globvars.vault_base, *args, **kwargs)

        self.isdead = False
        self.state= "0"

