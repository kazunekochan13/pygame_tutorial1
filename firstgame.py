# following tutorial by Tech With Tim @ youtube.com

import pygame
pygame.init() # always need this line in beginning of program to prevent error running

screen_x = 500
screen_y = 480
win = pygame.display.set_mode((screen_x, screen_y)) # creates a window and sets its dimensions

pygame.display.set_caption("First Game")

# load images
walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

x = 50
y = 400
width = 64
height = 64
vel = 5

isjump = False
jumpCount = 10

left = False
right = False
walkCount = 0

clock = pygame.time.Clock()

def redrawGameWindow():
	global walkCount # uses the walkCount variable from outside the scope of this function instead of instantiating a new one
	win.blit(bg, (0,0))
	
	if (walkCount + 1) >= 27:
		walkCount = 0;

	if left:
		win.blit(walkLeft[walkCount // 3], (x, y))
		walkCount += 1
	elif right:
		win.blit(walkRight[walkCount // 3], (x, y))
		walkCount += 1
	else:
		win.blit(char, (x,y))

	pygame.display.update() # refresh window

run = True
while run:

	clock.tick(27)
	
	for event in pygame.event.get(): # checking for events
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > 0:
		x -= vel
		left = True
		right = False
	elif keys[pygame.K_RIGHT] and x < (screen_x - width):
		x += vel
		right = True
		left = False
	else:
		left = right = False
		walkCount = 0
	if not(isjump):
		if keys[pygame.K_SPACE]:
			isjump = True
			left = False
			right = False
			walkCount = 0
	else:
		if jumpCount >= (-10):
			neg = 1
			if jumpCount < 0:
				neg = (-1)
			y -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -= 1
		else:
			isjump = False
			jumpCount = 10

	redrawGameWindow()

pygame.quit() # exit program