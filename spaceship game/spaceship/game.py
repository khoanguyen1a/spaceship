from __future__ import division
import pygame
import math
import random
import time

pygame.init()
width = 700
height = 700
size = (width,height)
fps = 120

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.Font('fonts/cargo.ttf',40)
score = pygame.font.Font('fonts/cargo.ttf',30)

background = pygame.image.load("images/bg5.jpg")
backrect = background.get_rect()
#author: Cuzco -> https://opengameart.org/content/space-background

ship = pygame.image.load("images/spaceship.png")
#author: Skorpio -> https://opengameart.org/content/spaceship-4
ship_width = 20

meteorr = pygame.transform.scale(pygame.image.load("images/Meteor1.png"),(100,75))
meteorr = pygame.transform.scale(pygame.image.load("images/Meteor2.png"),(100,75))
meteorr = pygame.transform.scale(pygame.image.load("images/Meteor3.png"),(100,75))
#author: Lluc Entertainment -> https://opengameart.org/content/meteor-animated-64x64

planetExplosion = pygame.mixer.Sound("sounds/mix.wav")
planetExplosion.set_volume(1)
#author: Unnamed -> https://opengameart.org/content/9-explosion-sounds

explosion = pygame.mixer.Sound("sounds/explosion.wav")
explosion.set_volume(2)
#author: TinyWorlds -> https://opengameart.org/content/explosion-0

countdown1 = pygame.mixer.Sound("sounds/countdown1.ogg")
countdown1.set_volume(1)
countdown1.play()

time.sleep(1)

countdown1 = pygame.mixer.Sound("sounds/countdown1.ogg")
countdown1.set_volume(1)
countdown1.play()

time.sleep(1)

countdown2 = pygame.mixer.Sound("sounds/countdown2.ogg")
countdown2.set_volume(1)
countdown2.play()
#author: Destructavator -> http://opengameart.org/content/countdown

time.sleep(1)

soundtrack = pygame.mixer.Sound("sounds/neocrey.mp3")
soundtrack.set_volume(0.5)
soundtrack.play(0)
#author: neocrey -> https://opengameart.org/content/neocrey-system-shock

def avoided(count):
	scoreFont = score.render("Score: %d" % count, True, (0,0,0))
	screen.blit(scoreFont, (50,570))

def meteor(meteor_x,meteor_y):
	screen.blit(meteorr,(meteor_x,meteor_y))




def car(x,y):
    screen.blit(ship,(x,y))



def car(x,y):
	screen.blit(ship,(x,y))

def message2(x):
	messageFont2 = font.render("You hit a meteor!", True, (0,0,0))
	rect = messageFont2.get_rect()
	rect.center = ((width//2),(height//2))
	screen.blit(messageFont2, rect)
	
	pygame.display.update()
	
	time.sleep(3)
	
	playing()	
	
def message(x):
	messageFont = font.render("You crashed into a another galaxy", True, (0,0,0))
	rect = messageFont.get_rect()
	rect.center = ((width//2),(height//2))
	screen.blit(messageFont, rect)
	
	pygame.display.update()
	
	time.sleep(3)
	
	playing()	
	
def crashed2():
	message2("You hit a Meteor!")

def crashed():
	message("You crashed into a another galaxy!")
	
def playing():
	x = 351
	y = 480 	

	xChange = 0
	yChange = 0
	meteor_x = random.randrange(50,770)
	meteor_y = -500
	meteor_speed = 2
	meteor_height = 45
	meteor_width = 70

	score = 0
	
	while True:
		
		clock.tick(fps)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					xChange = -6
				if event.key == pygame.K_RIGHT:
					xChange = 6
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					xChange = 0

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					yChange = 6
				if event.key == pygame.K_UP:
					yChange = -6
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					yChange = 0
					
		y += yChange

		x += xChange
		


		screen.blit(background, backrect)
		
		meteor(meteor_x,meteor_y)
		meteor_y += meteor_speed
		
		car(x,y)
		
		avoided(score)
		
		#crash detection if the spaceship goes off the road
		if x > (width - 10) or x < 50:
			planetExplosion.play()
			explosion.play()
			crashed()
		
		
		#starting the truck along random coordinates
		if meteor_y > height:
			meteor_y =- 45
			meteor_x = random.randrange(50,770)
			
			score += 1 #increase the score +1 for every truck is avoided
			meteor_speed += 0.3 #increase the speed by 0.2 for every truck passed
		
		#collision detection for hitting the truck
		if y < meteor_y + 45:
			
			if x > meteor_x and x < meteor_x + meteor_width or x + ship_width > meteor_x and x + ship_width < meteor_x + meteor_width:
				explosion.play()
				crashed2()
		
		pygame.display.flip()
	
playing()
