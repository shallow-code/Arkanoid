import pyglet

def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


pyglet.resource.path = ['resources',"resources\\im","resources\\im\\nemici","resources\\audio"]
pyglet.resource.reindex()

board_W=586
board_H=523
board_RLMargin=21

brick_W=42
brick_H=17
grid_W=27
grid_H=13
vault_W=73


speed_platform=500
speed_ball=400
speed_enemy=50


fase_of_game = 'crea_livello'

pallina_start=pyglet.resource.image("Palla_start.png")
pallina_im=pyglet.resource.image("PallaOriginal.png")

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
Vault_Base_1 = pyglet.resource.image("VausBaseOriginal1.png")
Vault_Base_2 = pyglet.resource.image("VausBaseOriginal2.png")
Vault_Base_3 = pyglet.resource.image("VausBaseOriginal3.png")

Vault_Crate_1=pyglet.resource.image("VausDissolviOriginal1.png")
Vault_Crate_2=pyglet.resource.image("VausDissolviOriginal2.png")
Vault_Crate_3=pyglet.resource.image("VausDissolviOriginal3.png")
#Vault_Crate_4=pyglet.resource.image("Vault_Dissolvi_3.png")
center_image(Vault_Base_1)
center_image(Vault_Base_2)
center_image(Vault_Base_3)
center_image(Vault_Crate_1)
center_image(Vault_Crate_2)
center_image(Vault_Crate_3)

seq_anim_vault_normal=[Vault_Base_1,Vault_Base_2,Vault_Base_3]
seq_anim_vault_create=[Vault_Crate_3,Vault_Crate_2,Vault_Crate_1]
seq_anim_vault_die=[Vault_Crate_1,Vault_Crate_2,Vault_Crate_3]

vault_anim_states={}
vault_anim_states["0"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_create, 0.35, loop=False)
vault_anim_states["1"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_normal, 0.25, loop=True)
vault_anim_states["2"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_die, 0.25, loop=False)


#mangione
Mangione=[]
Mangione.append(pyglet.resource.image("MangioneApre1.png"))
Mangione.append(pyglet.resource.image("MangioneApre2.png"))
Mangione.append(pyglet.resource.image("MangioneApre3.png"))
Mangione.append(pyglet.resource.image("MangioneApre4.png"))
Mangione.append(pyglet.resource.image("MangioneApre5.png"))
Mangione.append(pyglet.resource.image("MangioneApre4.png"))
Mangione.append(pyglet.resource.image("MangioneApre3.png"))
Mangione.append(pyglet.resource.image("MangioneApre2.png"))
Mangione.append(pyglet.resource.image("MangioneApre1.png"))

for m in Mangione:
	center_image(m)


Mangione_anim=pyglet.image.Animation.from_image_sequence(Mangione,0.25, loop=False)


#nemici
Enemies={}

Enemy_1=[]
Enemy_1.append(pyglet.resource.image("Enemy1_1.png"))
Enemy_1.append(pyglet.resource.image("Enemy1_2.png"))
Enemy_1.append(pyglet.resource.image("Enemy1_3.png"))
Enemy_1.append(pyglet.resource.image("Enemy1_4.png"))
Enemy_1.append(pyglet.resource.image("Enemy1_5.png"))
Enemy_1.append(pyglet.resource.image("Enemy1_6.png"))
Enemy_1.append(pyglet.resource.image("Enemy1_7.png"))
Enemy_1.append(pyglet.resource.image("Enemy1_8.png"))
Enemy_1.append(pyglet.resource.image("Enemy1_9.png"))
Enemy_1.append(pyglet.resource.image("Enemy1_10.png"))
Enemy_1.append(pyglet.resource.image("Enemy1_11.png"))
Enemy_1.append(pyglet.resource.image("Enemy1_12.png"))

EnemyExplosion=[]
EnemyExplosion.append(pyglet.resource.image("Enemy_Explosion_1.png"))
EnemyExplosion.append(pyglet.resource.image("Enemy_Explosion_2.png"))
EnemyExplosion.append(pyglet.resource.image("Enemy_Explosion_3.png"))
EnemyExplosion.append(pyglet.resource.image("Enemy_Explosion_4.png"))
EnemyExplosion.append(pyglet.resource.image("Enemy_Explosion_5.png"))
EnemyExplosion.append(pyglet.resource.image("Enemy_Explosion_6.png"))
EnemyExplosion.append(pyglet.resource.image("Enemy_Explosion_7.png"))
EnemyExplosion.append(pyglet.resource.image("Enemy_Explosion_8.png"))
EnemyExplosion.append(pyglet.resource.image("Enemy_Explosion_9.png"))
EnemyExplosion.append(pyglet.resource.image("Enemy_Explosion_10.png"))
EnemyExplosion.append(pyglet.resource.image("Enemy_Explosion_11.png"))
EnemyExplosion.append(pyglet.resource.image("Enemy_Explosion_12.png"))


for en in Enemy_1:
	center_image(en)

for en in EnemyExplosion:
	center_image(en)

Enemies["0"]=pyglet.image.Animation.from_image_sequence(Enemy_1,0.1, loop=True)
EnemyExplosion=pyglet.image.Animation.from_image_sequence(EnemyExplosion,0.2,loop=False)




lifes=5
global l_lifes
l_lifes=[]
vita_im=pyglet.resource.image("Vita.png")
center_image(vita_im)



background_image = pyglet.resource.image("Background1Original.png")


#vault images

main_batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
forestrings = pyglet.graphics.OrderedGroup(2)


hit_sound1 = pyglet.resource.media('Arkanoid 2 - Revenge of Doh SFX (HitSound1).wav', streaming=False)
hit_sound2 = pyglet.resource.media('Arkanoid 2 - Revenge of Doh SFX (HitSound2).wav', streaming=False)
hit_sound3 = pyglet.resource.media('Arkanoid 2 - Revenge of Doh SFX (HitSound3).wav', streaming=False)
die_sound = pyglet.resource.media('Arkanoid 2 - Revenge of Doh SFX (DieSound).wav', streaming=False)
die_alien_sound=pyglet.resource.media('Arkanoid 2 - Revenge of Doh SFX (AlienDestroyed).wav', streaming=False)



global flashes
flashes=[]

global alive_bricks
alive_bricks=[]

global vault
vault=None

global palline
palline=[]
global background_sprite

global alive_enemies
global numero_robini
numero_robini=0
alive_enemies=[]

global Mangioni 
Mangioni=[]