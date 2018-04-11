#Snake Game!

import pygame, sys, random, time

def gameOver():
	my_font = pygame.font.SysFont('monaco',72)
	GO_surf = my_font.render('Game over!', True, red)
	GO_rect = GO_surf.get_rect()
	GO_rect.midtop = (360, 15)
	play_surface.blit(GO_surf,GO_rect)
	pygame.display.flip()
	showScore(0)
	time.sleep(4)
	pygame.quit() #pygame exit
	sys.exit() #console exit

def showScore(show_in_corner = 1):
	score_font = pygame.font.SysFont('monaco',24)
	score_surf = score_font.render('Score : {0}'.format(score), True, black)
	score_rect = score_surf.get_rect()
	if show_in_corner == 1:
		score_rect.midtop = (80, 10)
	else:
		score_rect.midtop = (360, 120)
	play_surface.blit(score_surf, score_rect)


check_errors = pygame.init()
if check_errors[1] > 0:
	print("(!!!) Had {0} initiallzing errors, exiting...".format(check_errors[1]))
	sys.exit(-1)
else:
	print("Successful initialize!")

# Play surface
play_surface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game!')

# Color
red   = pygame.Color(255, 0, 0) #gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food

#FPS controller

fps_controller = pygame.time.Clock()
#snake & food variables
snake_pos  = [100, 50]
snake_body = [[100,50],[90,50],[90,50]]

food_pos   = [random.randrange(1,72)*10,random.randrange(1,46)*10]
food_spawn = True

score = 0

direction = 'RIGHT'
changeto  = direction


# game function
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				changeto ='RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				changeto ='LEFT'
			if event.key == pygame.K_UP or event.key == ord('w'):
				changeto ='UP'
			if event.key == pygame.K_DOWN or event.key == ord('s'):
				changeto ='DOWN'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))
	# validation od direction
	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction =  'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction =  'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction =  'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction =  'DOWN'

	if direction == 'RIGHT':
		snake_pos[0] += 10
	if direction == 'LEFT':
		snake_pos[0] -= 10
	if direction == 'UP':
		snake_pos[1] -= 10
	if direction == 'DOWN':
		snake_pos[1] += 10

	#snake body mechanism
	snake_body.insert(0, list(snake_pos))
	if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
		food_spawn = False
		score += 1
	else:
		snake_body.pop()

	if food_spawn == False:	
		food_pos   = [random.randrange(1,72)*10,random.randrange(1,46)*10]
	food_spawn = True
	# background
	play_surface.fill(white)
	# draw snake
	for pos in snake_body:
		pygame.draw.rect(play_surface, green, pygame.Rect(pos[0],pos[1],10,10))

	pygame.draw.rect(play_surface, brown, pygame.Rect(food_pos[0],food_pos[1],10,10))
	
	if snake_pos[0] > 710 or snake_pos[0] < 0 or snake_pos[1] > 450 or snake_pos[1] < 0:
		gameOver()
	for block in snake_body[1:]:
		if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
			gameOver()
		
	showScore()
	pygame.display.flip()
	fps_controller.tick(15)
	

