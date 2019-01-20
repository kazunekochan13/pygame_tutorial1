# following tutorial by Tech With Tim @ youtube.com

import pygame
pygame.init() # always need this line in beginning of program to prevent error running

screen_x = 500
screen_y = 500
win = pygame.display.set_mode((screen_x, screen_y)) # creates a window and sets its dimensions

pygame.display.set_caption("First Game")

x = 50
y = 450
width = 40
height = 60
vel = 5

isjump = True
jumpCount = 10

run = True
while run:
	pygame.time.delay(100) # in millisecond. acts as clock of game
	
	for event in pygame.event.get(): # checking for events
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > 0:
		x -= vel
	if keys[pygame.K_RIGHT] and x < (screen_x - width):
		x += vel
	if not(isjump):
		if keys[pygame.K_UP] and y > 0:
			y -= vel
		if keys[pygame.K_DOWN] and y < (screen_y - height):
			y += vel
		if keys[pygame.K_SPACE]:
			isjump = True
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

	win.fill((0, 0, 0))
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) # drawing character
	pygame.display.update() # refresh window

pygame.quit() # exit program