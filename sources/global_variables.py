import pyglet

def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


pyglet.resource.path = ['resources',"resources\\im","resources\\audio"]
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


fase_of_game = 'crea_livello'

pallina_start=pyglet.resource.image("Palla_start.png")
pallina_im=pyglet.resource.image("Palla_base.png")

center_image(pallina_im)
center_image(pallina_start)

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

Vault_Crate_1=pyglet.resource.image("Vault_Dissolvi_0.png")
Vault_Crate_2=pyglet.resource.image("Vault_Dissolvi_1.png")
Vault_Crate_3=pyglet.resource.image("Vault_Dissolvi_2.png")
Vault_Crate_4=pyglet.resource.image("Vault_Dissolvi_3.png")


center_image(Vault_Base_1)
center_image(Vault_Base_2)
center_image(Vault_Base_3)
center_image(Vault_Crate_1)
center_image(Vault_Crate_2)
center_image(Vault_Crate_3)
center_image(Vault_Crate_4)


seq_anim_vault_normal=[Vault_Base_1,Vault_Base_2,Vault_Base_3]
seq_anim_vault_create=[Vault_Crate_1,Vault_Crate_2,Vault_Crate_3,Vault_Crate_4]
seq_anim_vault_die=[Vault_Crate_4,Vault_Crate_3,Vault_Crate_2,Vault_Crate_1]

vault_anim_states={}
vault_anim_states["0"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_create, 0.35, loop=False)
vault_anim_states["1"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_normal, 0.25, loop=True)
vault_anim_states["2"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_die, 0.25, loop=False)


lifes=5
global l_lifes
l_lifes=[]
vita_im=pyglet.resource.image("Vita.png")
center_image(vita_im)



background_image = pyglet.resource.image("Background11.png")


#vault images
# vault_base=pyglet.resource.image("Vault_Base.png")
# center_image(vault_base)

main_batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
forestrings = pyglet.graphics.OrderedGroup(2)


hit_sound1 = pyglet.resource.media('Arkanoid 2 - Revenge of Doh SFX (HitSound1).wav', streaming=False)
hit_sound2 = pyglet.resource.media('Arkanoid 2 - Revenge of Doh SFX (HitSound2).wav', streaming=False)
hit_sound3 = pyglet.resource.media('Arkanoid 2 - Revenge of Doh SFX (HitSound3).wav', streaming=False)
die_sound = pyglet.resource.media('Arkanoid 2 - Revenge of Doh SFX (DieSound).wav', streaming=False)

global flashes
flashes=[]

global alive_bricks
alive_bricks=[]

global vault
vault=None
global palline
palline=[]
global background_sprite