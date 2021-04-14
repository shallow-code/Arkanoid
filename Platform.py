import pyglet
import pyglet.clock
import random
from pyglet.window import mouse
from pyglet.window import key


#starting settings
fase_of_game = 'main_game'
main_batch = pyglet.graphics.Batch()
window_height = 600
window_width = 600

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
platform_image = pyglet.resource.image("example_body.png")

def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

#centro immagini
center_image(platform_image)


#CLASS
#player
class Player(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



#stat game
Player = Player(img=platform_image, x=window_width//2 ,y=10+platform_image.height//2, batch = main_batch, group=foreground)
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


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()




# pyglet main loop
if __name__=='__main__':
    #pyglet.clock.schedule_interval(update, 1/5.0)
    pyglet.app.run()
