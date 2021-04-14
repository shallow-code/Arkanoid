import pyglet
import pyglet.clock
import random
from pyglet.window import mouse
from pyglet.window import key


#starting settings
fase_of_game = 'main_game'
main_batch = pyglet.graphics.Batch()
window_height = 400
window_width = 600
speed_platform = 500

#create window
game_window = pyglet.window.Window(window_width, window_height)
game_window.set_mouse_visible(False)
game_window.set_exclusive_mouse(True)

# order of images
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
forestrings = pyglet.graphics.OrderedGroup(2)
#path
pyglet.resource.path=['./resources']
pyglet.resource.reindex()



#load img
platform_image = pyglet.resource.image("Vault_Base_1.png")

Vault_Base_1 = pyglet.resource.image("Vault_Base_1.png")
Vault_Base_2 = pyglet.resource.image("Vault_Base_2.png")
Vault_Base_3 = pyglet.resource.image("Vault_Base_3.png")

seq_anim_vault=[Vault_Base_1,Vault_Base_2,Vault_Base_3]
vault_anim = pyglet.image.Animation.from_image_sequence(seq_anim_vault, 0.25, loop=True)



def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

#centro immagini
center_image(platform_image)

center_image(Vault_Base_1)
center_image(Vault_Base_2)
center_image(Vault_Base_3)

#CLASS
#player
class Player(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key_handler = key.KeyStateHandler()
        self.V_x = speed_platform

    def update(self,dt):
        if self.key_handler[key.LEFT]:
            self.x -= self.V_x * dt
            if self.x < platform_image.width//2:
                self.x=platform_image.width//2

        if self.key_handler[key.RIGHT]:
            self.x += self.V_x * dt
            if self.x > window_width - platform_image.width//2:
                self.x=window_width - platform_image.width//2


#stat game
Player = Player(img=vault_anim, x=window_width//2 ,y=10+platform_image.height//2, batch = main_batch, group=foreground)
print(window_width//2 ,10+platform_image.height//2)

#movement control
@game_window.event
def on_mouse_motion(x, y, dx, dy):
    if (fase_of_game == 'main_game'):
        Player.x += dx
        if Player.x < platform_image.width//2:
            Player.x = platform_image.width//2
        if Player.x > window_width - platform_image.width//2:
            Player.x = window_width - platform_image.width//2
        
#movement control
@game_window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if (fase_of_game == 'main_game'):
        Player.x += dx
        if Player.x < platform_image.width//2:
            Player.x = platform_image.width//2
        if Player.x > window_width - platform_image.width//2:
            Player.x = window_width - platform_image.width//2
            
#movement control
@game_window.event
def on_mouse_press(x, y, button, modifiers):
    if (fase_of_game == 'main_game'):
        if button == pyglet.window.mouse.LEFT:
            print("Click mouse")


#update positions
def update(dt):
    Player.update(dt)


#event handlers
game_window.push_handlers(Player.key_handler)
game_window.push_handlers(Player)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()




# pyglet main loop
if __name__=='__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
