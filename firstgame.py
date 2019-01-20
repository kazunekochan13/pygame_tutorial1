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

clock = pygame.time.Clock()

class player(object):

	def __init__(self, x, y , width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.isjump = False
		self.jumpCount = 10
		self.left = False
		self.right = False
		self.walkCount = 0

	def draw(self, win):
		if self.walkCount + 1 >= 27:
			self.walkCount = 0
		if self.left:
			win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
			self.walkCount += 1
		elif self.right:
			win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
			self.walkCount += 1
		else:
			win.blit(char, (self.x,self.y))

def redrawGameWindow():
	global walkCount # uses the walkCount variable from outside the scope of this function instead of instantiating a new one
	win.blit(bg, (0,0))
	
	man.draw(win)

	pygame.display.update() # refresh window


# main loop
man = player(300, 410, 64, 64)
run = True
while run:

	clock.tick(27)
	
	for event in pygame.event.get(): # checking for events
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and man.x > 0:
		man.x -= man.vel
		man.left = True
		man.right = False
	elif keys[pygame.K_RIGHT] and man.x < (screen_x - man.width):
		man.x += man.vel
		man.right = True
		man.left = False
	else:
		man.left = man.right = False
		man.walkCount = 0
	if not(man.isjump):
		if keys[pygame.K_SPACE]:
			man.isjump = True
			man.left = False
			man.right = False
			man.walkCount = 0
	else:
		if man.jumpCount >= (-10):
			neg = 1
			if man.jumpCount < 0:
				neg = (-1)
			man.y -= (man.jumpCount ** 2) * 0.5 * neg
			man.jumpCount -= 1
		else:
			man.isjump = False
			man.jumpCount = 10

	redrawGameWindow()

pygame.quit() # exit program