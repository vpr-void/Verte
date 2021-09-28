import pygame
import sys
from pygame.locals import *
import pygame.freetype

clck = pygame.time.Clock()
pygame.mixer.pre_init(44100, -16, 2, 1000)
pygame.init()
pygame.freetype.init()
win_size = (600,400)
screenS = pygame.display.set_mode(win_size,0,32)
display = pygame.Surface((600,400))
pygame.display.set_caption('Platf_ kinda thingy')

font_1 = pygame.freetype.Font('04b_30_.TTF',20)
font_2 = pygame.freetype.Font('04b_30_.TTF',15)
font_3 = pygame.freetype.Font('04b_30_.TTF',13)
menu_on = True
game_start = False

# img
bg_img = pygame.image.load('objs&maps/2 Background/Background.png')
bg_img = pygame.transform.scale(bg_img,(600,400))

one_ = pygame.image.load('objs&maps/1 Tiles/Tile_12.png')
two_ = pygame.image.load('objs&maps/1 Tiles/Tile_02.png')

three_ = pygame.image.load('objs&maps/1 Tiles/Tile_03.png')
three_ = pygame.image.load('objs&maps/1 Tiles/Tile_03.png').convert()


four_ = pygame.image.load('objs&maps/1 Tiles/Tile_01.png')
four_ = pygame.image.load('objs&maps/1 Tiles/Tile_01.png').convert()


five_ = pygame.image.load('objs&maps/1 Tiles/Tile_24.png')
six_ = pygame.image.load('objs&maps/1 Tiles/Tile_26.png')

seven_ = pygame.image.load('objs&maps/1 Tiles/Tile_07.png')



eight_ = pygame.image.load('objs&maps/1 Tiles/Tile_08.png')



nine_ = pygame.image.load('objs&maps/1 Tiles/Tile_09.png')


ll_ = pygame.image.load('objs&maps/1 Tiles/Tile_32.png')
mm_ = pygame.image.load('objs&maps/1 Tiles/Tile_33.png')
nn_ = pygame.image.load('objs&maps/1 Tiles/Tile_34.png')
qq_ = pygame.image.load('objs&maps/1 Tiles/Tile_13.png')
rr_ = pygame.image.load('objs&maps/1 Tiles/Tile_11.png')
oo_ = pygame.image.load('objs&maps/1 Tiles/Tile_39.png')

cloud_1 = pygame.image.load('objs&maps/2 Background/c1.png')
cloud_1.set_colorkey((146,244,255))
cloud_2 = pygame.image.load('objs&maps/2 Background/c2.png')
cloud_2.set_colorkey((146,244,255))

tree_ = pygame.image.load('objs&maps/3 objects/willows/3.png')
box1_ = pygame.image.load('objs&maps/3 objects/boxes/4.png')
px_ = pygame.image.load('objs&maps/3 objects/pointers/1.png')
pointer_ = pygame.image.load('objs&maps/3 objects/pointers/7.png')
bush1_ = pygame.image.load('objs&maps/3 objects/bushes/7.png') 
g1_ = pygame.image.load('objs&maps/3 objects/grass/1.png')
g2_ = pygame.image.load('objs&maps/3 objects/grass/2.png')
g3_ = pygame.image.load('objs&maps/3 objects/grass/3.png')
stone_ = pygame.image.load('objs&maps/3 objects/stones/2.png')
stone2_ = pygame.image.load('objs&maps/3 objects/stones/5.png')
tree2_ = pygame.image.load('objs&maps/3 objects/willows/2.png')

sp_ = pygame.image.load('objs&maps/3 objects/spike.png')
sp_ = pygame.transform.scale(sp_,(25,25))
sp_.set_colorkey((255,255,255))

s2_ = pygame.image.load('objs&maps/3 objects/S2.png')
s2_.set_colorkey((255,255,255))


e_img = pygame.image.load('character/3 Dude_Monster/dude_monster_2.png')
e_img.set_colorkey((255,255,255))
e_img_1 = pygame.image.load('character/3 Dude_Monster/dude_monster_1.png')
e_img_1.set_colorkey((255,255,255))
e_img_2 = pygame.image.load('character/3 Dude_Monster/dude_monster_2.png')

e_img_2.set_colorkey((255,255,255))

c_img = pygame.image.load('character/2 Owlet_Monster/coin/coin_0.png')
# c_img = pygame.transform.scale(c_img,(30,30))
# c_img.set_colorkey((255,255,255))

p_img = pygame.image.load('character/1 Pink_Monster/Pink_Monster.png').convert()

# p_img = pygame.transform.scale(p_img,(32,32))
# p_img.set_colorkey((255,255,255))

# sounds
j_sound = pygame.mixer.Sound('musics/jump.wav')
j_sound.set_volume(0.2)
pygame.mixer.music.load('musics/game2cut.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

c_sound = pygame.mixer.Sound('musics/coin.wav')
c_sound.set_volume(0.2)


# kinda physics
m_r = False
m_l = False
y_momentum = 0
air_timer = 0

p_action = 'idle'
p_frame = 0
p_flip = False

c_action = 'coin'
c_frame = 0

p_rect = pygame.Rect(420,250,20,30)# 420 original
m_tile = pygame.Rect(320,288,32,32)


true_scroll = [0,0]

def load_map(path):
	
	f = open(path + '.txt' , 'r')
	data = f.read()
	f.close()
	data = data.split('\n')
	game_map = []
	for row in data:
		game_map.append(list(row))
	return game_map

game_map = load_map('map_shit')
solid_tiles = ['0','p','b','B','v','g','G','&','7','8','9','1','c','y']
half_tiles = ['7','8','9']

bg_objects = [[0.25,[240,20,330,200]],[0.25,[560,60,80,80]],[0.5,[60,80,300,150]],[0.5,[260,180,400,80]],[0.5,[600,160,450,130]],   [0.25,[840,20,330,200]],[0.25,[1160,60,80,80]],[0.5,[960,80,300,150]],[0.5,[860,180,400,80]],[0.5,[1200,160,450,130]],   [0.25,[1440,20,330,200]],[0.25,[1760,60,80,80]],[0.5,[1560,80,300,150]],[0.5,[1460,180,400,80]],[0.5,[1800,160,450,130]],   [0.25,[2040,20,330,200]],[0.25,[2360,60,80,80]],[0.5,[2160,80,300,150]],[0.5,[2660,180,400,80]],[0.5,[2400,160,450,130]]]

coins = [[[580,230,20,20],0],[[610,230,20,20],0],[[640,230,20,20],0],[[1628,230,20,20],0],[[1658,230,20,20],0],[[1688,230,20,20],0],[[1718,230,20,20],0],[[1748,230,20,20],0],[[2308,330,20,20],0],[[2402,265,20,20],0],[[3555,170,20,20],0],[[3585,170,20,20],0],[[3615,170,20,20],0],[[4180,170,20,20],0],[[4210,170,20,20],0],[[4240,170,20,20],0],[[4270,170,20,20],0],[[4835,230,20,20],0],[[4932,170,20,20],0]]

# auto_move_tiles_1 = [2528,352,32,32]
# auto_move_tiles_2 = [2552,290,32,32]
am_1a = pygame.Rect(2528,352,32,32)
am_1b = pygame.Rect(2560,352,32,32)
am_2a = pygame.Rect(2650,290,32,32)
am_2b = pygame.Rect(2682,290,32,32)
am_r = True
am_l = False


cpt1 = pygame.Rect(2018,350,32,16)
cpt1m = False

cpt2 = pygame.Rect(3196,352,32,16)
cpt2m = False

cpt3 = pygame.Rect(3964,320,32,16)
cpt3m = False

cpt4 = pygame.Rect(4440,194,32,16)
cpt4m = False

cpt5 = pygame.Rect(5116,258,32,16)
cpt5m = False

global animation_frames
animation_frames = {}
def load_animation(path,frame_durations):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_durations:
        animation_frame_id = animation_name + '_' + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        # player_animations/idle/idle_0.png
        animation_image = pygame.image.load(img_loc).convert()
        animation_image.set_colorkey((255,255,255))
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data


def change_action(action_var,frame,new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var,frame
        

animation_database = {}

animation_database['run'] = load_animation('character/2 Owlet_Monster/run',[20,20])
animation_database['idle'] = load_animation('character/2 Owlet_Monster/idle',[10,10,20])
animation_database['jump'] = load_animation('character/2 Owlet_Monster/jump',[5,5,100])
animation_database['coin'] = load_animation('character/2 Owlet_Monster/coin',[10,10,20])



# def changePlaceTile(img,posit_x,posit_y,m_coords,p_posit,scrollx,scrolly,player):

# 	t_rect = pygame.Rect(posit_x,posit_y,32,16)
# 	display.blit(img,(posit_x-scrollx,posit_y-scrolly))
# 	return t_rect

	


s_quit = False

def collisions_test(rect,tiles):

	hit_list = []
	for tile in tiles:
		if rect.colliderect(tile):
			hit_list.append(tile)

	return hit_list


def move(rect,movement,tiles):
	
	collisions_types = {'top':False,'bottom':False,'right':False,'left':False}
	rect.x += movement[0]
	hit_list = collisions_test(rect,tiles)
	for tile in hit_list:
		if movement[0] > 0 :
			rect.right = tile.left
			collisions_types['right'] = True
		elif movement[0] < 0 :
			rect.left = tile.right
			collisions_types['left'] = True
	rect.y += movement[1]
	hit_list = collisions_test(rect,tiles)
	for tile in hit_list:
		if movement[1] > 0 :
			rect.bottom = tile.top
			collisions_types['bottom'] = True
		elif movement[1] < 0 :
			rect.top = tile.bottom
			collisions_types['top'] = True

	return rect,collisions_types


enemies = [[[1800,322,20,30],1400,1900],[[3000,322,20,30],2850,3050]]
e_mr = True
e_ml = False




text_dis = True

p_lives = 5

while True:
	

	# screenS.blit(bg_img,(0,0))
	# display.blit(bg_img,(0,0))
	display.fill((146,244,255))
	

	true_scroll[0] += (p_rect.x - true_scroll[0]-305)/20
	true_scroll[1] += (p_rect.y - true_scroll[1]-213)/20
	scroll = true_scroll.copy()
	scroll[0] = int(scroll[0])
	scroll[1] = int(scroll[1])

	# pygame.draw.rect(display,(0,176,196),pygame.Rect(0,240,600,160))
	# display.blit(cloud_1,(100,100))
	for bg_object in bg_objects:
		# for i in range(3):
		obj_rect = pygame.Rect(bg_object[1][0] - scroll[0]*bg_object[0],bg_object[1][1] - scroll[1]*bg_object[0],bg_object[1][2],bg_object[1][3])

		if bg_object[0] == 0.5:
			display.blit(cloud_1,(obj_rect))
		else :
			display.blit(cloud_2,(obj_rect))


	coin_count = 0
	for coin in coins:
		c_rect = pygame.Rect(coin[0][0],coin[0][1],coin[0][2],coin[0][3])
		
		if p_rect.colliderect(c_rect):
			 coin[0][1] = 1000
			 coin[1] = 1
			 c_sound.play()	 
		display.blit(c_img,(c_rect.x-scroll[0],c_rect.y-scroll[1]))
		coin_count += coin[1]
	display.blit(c_img,(540,10))
	font_1.render_to(display,(570,10),str(coin_count),(27,69,73))

	for e in enemies:
		e_rect = pygame.Rect(e[0][0],e[0][1],e[0][2],e[0][3])

		if e[0][0] == e[2]:
			e_img = e_img_1
			e_mr = False
			e_ml = True
			
		elif e[0][0] == e[1]:
			e_img = e_img_2
			e_mr = True
			e_ml = False

		if e_mr == True:
			e[0][0] += 1
		if e_ml == True:
			e[0][0] -= 1


		display.blit(e_img,(e_rect.x-scroll[0],e_rect.y-scroll[1]))

		if p_rect.colliderect(e_rect):
			p_rect = pygame.Rect(420,250,20,30)
			cpt1 = pygame.Rect(2018,350,32,16)
			cpt2 = pygame.Rect(3196,352,32,16)
			cpt3 = pygame.Rect(3964,320,32,16)
			cpt4 = pygame.Rect(4440,194,32,16)
			cpt5 = pygame.Rect(5116,258,32,16)
			p_lives -= 1




	display.blit(s2_,(10,10))
	font_1.render_to(display,(43,13),str(p_lives),(27,69,73))






	tile_rects = []
	y = 0
	for layer in game_map:
		x = 0
		for tile in layer:
			if tile == '1':
				display.blit(one_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == '2':
				display.blit(two_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == '3':
				display.blit(three_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == '4':
				display.blit(four_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == '5':
				display.blit(five_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == '6':
				display.blit(six_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == '7':
				display.blit(seven_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == '8':
				display.blit(eight_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == '9':
				display.blit(nine_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == 'l':
				display.blit(ll_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == 'm':
				display.blit(mm_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == 'n':
				display.blit(nn_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == 'q':
				display.blit(qq_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == 'r':
				display.blit(rr_,(x*32-scroll[0],y*32-scroll[1]))
			if tile == 'o':
				display.blit(oo_,(x*32-scroll[0],y*32-scroll[1]))
			# if tile == 'c':
			# 	c_rect = pygame.Rect(x*32.5,y*34,20,20)
			# 	c_action,c_frame = change_action(c_action,c_frame,'coin')
			# 	display.blit(c_img,(c_rect.x-scroll[0],c_rect.y-scroll[1]))
			
			if tile == 'y':
				display.blit(sp_,(x*32-scroll[0],y*32.5-scroll[1]))
				sp_rect = pygame.Rect(x*32,y*32,32,15)
				# tile_rects.append(sp_rect)
				if p_rect.colliderect(sp_rect):
					p_rect = pygame.Rect(420,250,20,30)
					cpt1 = pygame.Rect(2018,350,32,16)
					cpt2 = pygame.Rect(3196,352,32,16)
					cpt3 = pygame.Rect(3964,320,32,16)
					cpt4 = pygame.Rect(4440,194,32,16)
					cpt5 = pygame.Rect(5116,258,32,16)
					p_lives -= 1
			if tile == 't':
				display.blit(tree_,(x*22-scroll[0],y*17-scroll[1]))
			if tile == 'p':
				display.blit(pointer_,(x*42-scroll[0],y*33.5-scroll[1]))
			if tile == 'B':
				display.blit(bush1_,(x*35-scroll[0],y*32.9-scroll[1]))
			if tile == 'b':
				display.blit(box1_,(x*39-scroll[0],y*32.8-scroll[1]))
			if tile == 'v':
				display.blit(px_,(x*36-scroll[0],y*33.2-scroll[1]))
			if tile == 'g':
				display.blit(g1_,(x*42-scroll[0],y*33.5-scroll[1]))
			if tile == 'G':
				display.blit(g2_,(x*40-scroll[0],y*33.6-scroll[1]))
			if tile == '&':
				display.blit(g3_,(x*32-scroll[0],y*33.6-scroll[1]))

			if tile not in solid_tiles:
				tile_rects.append(pygame.Rect(x*32,y*32,32,32))
			if tile in half_tiles:
				tile_rects.append(pygame.Rect(x*32,y*32,32,10))
			x += 1
		y += 1
	

	tile_rects.append(am_1a)
	tile_rects.append(am_1b)
	tile_rects.append(am_2a)
	tile_rects.append(am_2b)
	display.blit(seven_,(am_1a.x-scroll[0],am_1a.y-scroll[1]))	
	display.blit(nine_,(am_1b.x-scroll[0],am_1b.y-scroll[1]))	
	display.blit(seven_,(am_2a.x-scroll[0],am_2a.y-scroll[1]))
	display.blit(nine_,(am_2b.x-scroll[0],am_2b.y-scroll[1]))
	if am_1a.x == 2528 and am_2a.x == 2650:
		am_r = True
		am_l = False
	if am_1b.x == 2618 and am_2b.x == 2740:
		am_r = False
		am_l = True

	if am_r == True:
		am_1a.x += 1
		am_1b.x += 1
		am_2a.x += 1
		am_2b.x += 1
	elif am_l == True:
		am_1a.x -= 1
		am_1b.x -= 1
		am_2a.x -= 1
		am_2b.x -= 1



	tile_rects.append(cpt1)
	display.blit(oo_,(cpt1.x-scroll[0],cpt1.y-scroll[1]))
	if p_rect.x > cpt1.x - 13 and cpt1.x > 1930:
		cpt1.x -= 5

	tile_rects.append(cpt2)
	display.blit(oo_,(cpt2.x-scroll[0],cpt2.y-scroll[1]))
	if p_rect.x > cpt2.x - 13 and cpt2.x > 3108:
		cpt2.x -= 5

	tile_rects.append(cpt3)
	display.blit(oo_,(cpt3.x-scroll[0],cpt3.y-scroll[1]))
	if p_rect.x > cpt3.x - 5 and cpt3.y < 1000:
		cpt3.y += 5

	tile_rects.append(cpt4)
	display.blit(oo_,(cpt4.x-scroll[0],cpt4.y-scroll[1]))
	if p_rect.x > cpt4.x - 25 and cpt4.x < 4530:
		cpt4.x += 5

	tile_rects.append(cpt5)
	display.blit(oo_,(cpt5.x-scroll[0],cpt5.y-scroll[1]))
	if p_rect.x > cpt5.x - 5 and cpt5.y < 1000:
		cpt5.y += 5


	# if p_rect.colliderect(c_rect) and cc == 0:
	# 	print('got coin')
	# if text_dis == True:
	# 	font_2.render_to(display,(50,50), 'Press arrow keys to move!',(102,114,145))
	# 	font_2.render_to(display,(50,64), 'Space to Jump!',(102,114,145))
	# pygame.time.delay(3000)
	# text_dis = False



	# if p_rect.x > 3200:
	# 	print(p_rect)

	



	p_movement = [0,0]
	if m_r == True and p_rect.x < 5500:
		p_movement[0] += 4
	if m_l == True and p_rect.x > 450:
		p_movement[0] -= 4
	p_movement[1] += y_momentum
	y_momentum += 0.4
	if y_momentum > 6:
		y_momentum = 6	


	if p_rect.x > 250 :
		
		m_tile.x += 6
		if m_tile.x > 480:
			m_tile.x = 480
	else:
		m_tile.x -= 6
		if m_tile.x < 320:
			m_tile.x = 320


	p_rect,collisions = move(p_rect,p_movement,tile_rects)


	if p_movement[0] == 0:
		p_action,p_frame = change_action(p_action,p_frame,'idle')
	if p_movement[0] > 0:
		p_action,p_frame = change_action(p_action,p_frame,'run')
		p_flip = False
	if p_movement[0] < 0:
		p_action,p_frame = change_action(p_action,p_frame,'run')
		p_flip = True
	if y_momentum < 0:
		p_action,p_frame = change_action(p_action,p_frame,'jump')



	if collisions['bottom'] == True:
		y_momentum = 0
		air_timer = 0
	else:
		air_timer += 2



	

	p_frame += 1
	if p_frame >= len(animation_database[p_action]):
		p_frame = 0
	p_img_id = animation_database[p_action][p_frame]
	p_img = animation_frames[p_img_id]


	c_frame += 1
	if c_frame >= len(animation_database[c_action]):
		c_frame = 0
	c_img_id = animation_database[c_action][c_frame]
	c_img = animation_frames[c_img_id]







	display.blit(px_,(5280-scroll[0],300-scroll[1]))
	
	display.blit(stone_,(5500-scroll[0],264-scroll[1]))

	display.blit(pygame.transform.flip(p_img,p_flip,False),(p_rect.x-scroll[0],p_rect.y-scroll[1]))

	display.blit(bush1_,(5550-scroll[0],297-scroll[1]))
	display.blit(tree_,(5500-scroll[0],138-scroll[1]))
	display.blit(g1_,(5600-scroll[0],304-scroll[1]))
	display.blit(g2_,(5550-scroll[0],304-scroll[1]))
	display.blit(g3_,(5485-scroll[0],304-scroll[1]))
	display.blit(g1_,(5600-scroll[0],304-scroll[1])) 

	if text_dis == True:
		font_2.render_to(display,(30,50),'Press arrow keys to move!',(38,38,79,80))
		font_2.render_to(display,(30,65),'Space to jump!',(38,38,79,80))
	if p_rect.x > 1000:
		text_dis = False

	if p_lives == 0 :
		font_1.render_to(display,(40,40),'lol nigga U suck ...',(27,69,73))
		font_3.render_to(display,(40,300),'Automatically quit after u pass that floating tile',(146,244,255))
		if p_rect.x > 700:
			pygame.quit()



	if p_rect.x >= 5500:
		# font_1.render_to(display,(150,150),'U did it mathafakaa !!!',(93,93,93))
		font_1.render_to(display,(10,50),'U did it mathafakaa !!!',(38,38,79))
		font_2.render_to(display,(10,70),'Jump to QUIT!',(50,50,50,90))
		if y_momentum < -5:
			s_quit = True

	

	for event in pygame.event.get():
		if event.type == QUIT or s_quit == True:
			
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				m_r = True
			if event.key == K_LEFT:
				m_l = True
			if event.key == K_SPACE:
				if air_timer < 12 :
					j_sound.play()
					y_momentum -= 10
		if event.type == KEYUP:
			if event.key == K_RIGHT:
				m_r = False
			if event.key == K_LEFT:
				m_l = False

	screenS.blit(pygame.transform.scale(display,win_size),(0,0))
	pygame.display.update()
	clck.tick(60)