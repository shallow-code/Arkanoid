import pyglet

def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


pyglet.resource.path = ['resources',"resources\\im","resources\\im\\nemici","resources\\im\\powers","resources\\audio"]
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
speed_ball=300
speed_enemy=50


fase_of_game = 'crea_livello'

pallina_start=pyglet.resource.image("Palla_start.png")
pallina_im=pyglet.resource.image("PallaOriginal.png")
pallina_nera=pyglet.resource.image("PallaNera.png")

center_image(pallina_im)
center_image(pallina_start)
center_image(pallina_nera)

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

Vault_E_1 = pyglet.resource.image("Vaus_E1.png")
Vault_E_2 = pyglet.resource.image("Vaus_E2.png")
Vault_E_3 = pyglet.resource.image("Vaus_E3.png")

Vault_R_1 = pyglet.resource.image("Vaus_R1.png")
Vault_R_2 = pyglet.resource.image("Vaus_R2.png")
Vault_R_3 = pyglet.resource.image("Vaus_R3.png")

Vault_T_1 = pyglet.resource.image("Vaus_T1.png")
Vault_T_2 = pyglet.resource.image("Vaus_T2.png")
Vault_T_3 = pyglet.resource.image("Vaus_T3.png")

Vault_Crate_1=pyglet.resource.image("VausDissolviOriginal1.png")
Vault_Crate_2=pyglet.resource.image("VausDissolviOriginal2.png")
Vault_Crate_3=pyglet.resource.image("VausDissolviOriginal3.png")


Vault_Shadow_D1 = pyglet.resource.image("Shadow_D1.png")
Vault_Shadow_D2 = pyglet.resource.image("Shadow_D2.png")
Vault_Shadow_S1 = pyglet.resource.image("Shadow_S1.png")
Vault_Shadow_S2 = pyglet.resource.image("Shadow_S2.png")


center_image(Vault_Base_1)
center_image(Vault_Base_2)
center_image(Vault_Base_3)
center_image(Vault_Crate_1)
center_image(Vault_Crate_2)
center_image(Vault_Crate_3)
center_image(Vault_E_1)
center_image(Vault_E_2)
center_image(Vault_E_3)

center_image(Vault_R_1)
center_image(Vault_R_2)
center_image(Vault_R_3)

center_image(Vault_T_1)
center_image(Vault_T_2)
center_image(Vault_T_3)

center_image(Vault_Shadow_D1)
center_image(Vault_Shadow_D2)
center_image(Vault_Shadow_S1)
center_image(Vault_Shadow_S2)

VausShadows_im={}
VausShadows_im["D1"]=Vault_Shadow_D1
VausShadows_im["D2"]=Vault_Shadow_D2
VausShadows_im["S1"]=Vault_Shadow_S1
VausShadows_im["S2"]=Vault_Shadow_S2


seq_anim_vault_normal=[Vault_Base_1,Vault_Base_2,Vault_Base_3]
seq_anim_vault_E=[Vault_E_1,Vault_E_2,Vault_E_3]
seq_anim_vault_R=[Vault_R_1,Vault_R_2,Vault_R_3]
seq_anim_vault_T=[Vault_T_1,Vault_T_2,Vault_T_3]

seq_anim_vault_create=[Vault_Crate_3,Vault_Crate_2,Vault_Crate_1]
seq_anim_vault_die=[Vault_Crate_1,Vault_Crate_2,Vault_Crate_3]

vault_anim_states={}
vault_anim_states["0"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_create, 0.35, loop=False)
vault_anim_states["1"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_normal, 0.25, loop=True)
vault_anim_states["2"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_die, 0.25, loop=False)
vault_anim_states["E"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_E, 0.25, loop=True)
vault_anim_states["R"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_R, 0.25, loop=True)
vault_anim_states["T"] = pyglet.image.Animation.from_image_sequence(seq_anim_vault_T, 0.25, loop=True)


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


#powerups

PowerUP={}
all_Powers=["N","M","E","R","T","I","D","S"]

for P in all_Powers:
	l_P=[]
	l_P.append(pyglet.resource.image(P+"1.png"))
	l_P.append(pyglet.resource.image(P+"2.png"))
	l_P.append(pyglet.resource.image(P+"3.png"))
	l_P.append(pyglet.resource.image(P+"4.png"))
	l_P.append(pyglet.resource.image(P+"5.png"))
	l_P.append(pyglet.resource.image(P+"6.png"))

	for el in l_P:
		center_image(el)

	PowerUP[P]=pyglet.image.Animation.from_image_sequence(l_P,0.2,loop=True)







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
forestrings1 = pyglet.graphics.OrderedGroup(3)

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

global GamePowerUpState
GamePowerUpState=None

global alive_powerups
alive_powerups=[]

global Vaus_Shadows
Vaus_Shadows={}
