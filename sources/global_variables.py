import pyglet

pyglet.resource.path = ['resources']
pyglet.resource.reindex()

board_W=546
board_H=459
brick_W=42
brick_H=17
grid_W=27
grid_H=13


bricks_im={}
bricks_im["1"]= pyglet.resource.image("Type1.png")
bricks_im["2R"] = pyglet.resource.image("Type2R.png")
bricks_im["2Y"] = pyglet.resource.image("Type2Y.png")
bricks_im["2B"] = pyglet.resource.image("Type2B.png")
bricks_im["2A"] = pyglet.resource.image("Type2A.png")
bricks_im["3"] = pyglet.resource.image("Type3.png")
bricks_im["4"] = pyglet.resource.image("Type4.png")

background_image = pyglet.resource.image("Background1.png")

main_batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
