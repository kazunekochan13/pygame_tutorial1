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
		self.standing = True
		self.hitbox = (self.x + 17, self.y + 11, 29, 52)

	def draw(self, win):
		if (self.walkCount + 1) >= 27:
			self.walkCount = 0
		if not(self.standing):
			if self.left:
				win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
				self.walkCount += 1
			elif self.right:
				win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
				self.walkCount += 1
		else:
			if self.right:
				win.blit(walkRight[0], (self.x, self.y))
			else:
				win.blit(walkLeft[0], (self.x, self.y))
		self.hitbox = (self.x + 17, self.y + 11, 29, 52)
		pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class projectile(object):

	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.vel = 8 * facing

	def draw(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class enemy(object):
	walkRight = [pygame.image.load('Game/R1E.png'), pygame.image.load('Game/R2E.png'), pygame.image.load('Game/R3E.png'), pygame.image.load('Game/R4E.png'), pygame.image.load('Game/R5E.png'), pygame.image.load('Game/R6E.png'), pygame.image.load('Game/R7E.png'), pygame.image.load('Game/R8E.png'), pygame.image.load('Game/R9E.png'), pygame.image.load('Game/R10E.png'), pygame.image.load('Game/R11E.png')]
	walkLeft = [pygame.image.load('Game/L1E.png'), pygame.image.load('Game/L2E.png'), pygame.image.load('Game/L3E.png'), pygame.image.load('Game/L4E.png'), pygame.image.load('Game/L5E.png'), pygame.image.load('Game/L6E.png'), pygame.image.load('Game/L7E.png'), pygame.image.load('Game/L8E.png'), pygame.image.load('Game/L9E.png'), pygame.image.load('Game/L10E.png'), pygame.image.load('Game/L11E.png')]
 
	def __init__(self, x, y, width, height, end):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		self.path = (self.x, self.end)
		self.walkCount = 0
		self.vel = 3
		self.hitbox = (self.x + 17, self.y + 2, 31, 57)

	def draw(self, win):
		self.move()
		if (self.walkCount + 1) >= 33:
			self.walkCount = 0
		if self.vel > 0:
			win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
			self.walkCount += 1
		else:
			win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
			self.walkCount += 1
		self.hitbox = (self.x + 17, self.y + 2, 31, 57)
		pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

	def move(self):
		if self.vel > 0: # going right
			if (self.x + self.vel) < self.path[1]:
				self.x += self.vel
			else:
				self.vel = self.vel * (-1)
				self.walkCount = 0
		else: # going left
			if (self.x - self.vel) > self.path[0]:
				self.x += self.vel
			else:
				self.vel = self.vel * (-1)
				self.walkCount = 0

	def hit(self):
		print("hit")
		pass

def redrawGameWindow():
	global walkCount # uses the walkCount variable from outside the scope of this function instead of instantiating a new one
	win.blit(bg, (0,0))
	
	man.draw(win)
	for bullet in bullets:
		bullet.draw(win)
	goblin.draw(win)
	pygame.display.update() # refresh window


# main loop
man = player(300, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450)
shootloop = 0
bullets = []
run = True
while run:

	clock.tick(27)
	
	if shootloop > 0:
		shootloop += 1
	if shootloop > 3:
		shootloop = 0

	for event in pygame.event.get(): # checking for events
		if event.type == pygame.QUIT:
			run = False

	for bullet in bullets:
		if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
			if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[3]:
				goblin.hit()
				bullets.pop(bullets.index(bullet))
		if bullet.x < screen_x and bullet.x > 0:
			bullet.x += bullet.vel
		else:
			bullets.pop(bullets.index(bullet))

	keys = pygame.key.get_pressed()

	if keys[pygame.K_SPACE] and shootloop == 0:
		if man.left:
			facing = (-1)
		else:
			facing = 1
		if len(bullets) < 5:
			bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))
		shootloop = 1
	if keys[pygame.K_LEFT] and man.x > 0:
		man.x -= man.vel
		man.left = True
		man.right = False
		man.standing = False
	elif keys[pygame.K_RIGHT] and man.x < (screen_x - man.width):
		man.x += man.vel
		man.right = True
		man.left = False
		man.standing = False
	else:
		man.standing = True
		man.walkCount = 0
	if not(man.isjump):
		if keys[pygame.K_UP]:
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