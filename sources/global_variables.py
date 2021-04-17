import pyglet

def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


pyglet.resource.path = ['resources']
pyglet.resource.reindex()

board_W=546
board_H=459
brick_W=42
brick_H=17
grid_W=27
grid_H=13
vault_W=73


speed_platform=500
speed_ball=400


pallina_im=pyglet.resource.image("Palla_base.png")
center_image(pallina_im)

bricks_im={}
bricks_im["1"]= pyglet.resource.image("Type1.png")
bricks_im["2R"] = pyglet.resource.image("Type2R.png")
bricks_im["2Y"] = pyglet.resource.image("Type2Y.png")
bricks_im["2B"] = pyglet.resource.image("Type2B.png")
bricks_im["2A"] = pyglet.resource.image("Type2A.png")
bricks_im["2W"] = pyglet.resource.image("Type2W.png")
bricks_im["3"] = pyglet.resource.image("Type3.png")
bricks_im["4"] = pyglet.resource.image("Type4.png")

for key in bricks_im.keys():
	center_image(bricks_im[key])

#immagini navicella
Vault_Base_1 = pyglet.resource.image("Vault_Base_1.png")
Vault_Base_2 = pyglet.resource.image("Vault_Base_2.png")
Vault_Base_3 = pyglet.resource.image("Vault_Base_3.png")
center_image(Vault_Base_1)
center_image(Vault_Base_2)
center_image(Vault_Base_3)
seq_anim_vault_normal=[Vault_Base_1,Vault_Base_2,Vault_Base_3]
vault_anim_states={}
vault_anim_states["0"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_normal, 0.25, loop=True)


background_image = pyglet.resource.image("Background11.png")


#vault images
vault_base=pyglet.resource.image("Vault_Base.png")
center_image(vault_base)

main_batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
forestrings = pyglet.graphics.OrderedGroup(2)

global flashes
flashes=[]

global alive_bricks
alive_bricks=[]
