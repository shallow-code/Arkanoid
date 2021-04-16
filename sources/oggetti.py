import pyglet
import sources.global_variables as globvars
from pyglet.window import key

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
