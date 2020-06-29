import pygame
import random

class Enemy(pygame.sprite.Sprite):
	walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), 	pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
	walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]



	def __init__(self, x ,y ):
		pygame.sprite.Sprite.__init__(self)		
		self.image = pygame.image.load('L1E.png')		
		self.ememy_sprites = pygame.sprite.Group()		
			
		self.x = 200
		self.y = 500
		self.rect = self.image.get_rect()		
		self.rect.x = x	
		self.rect.y = y
		self.width = 400
		self.height = 600
		self.path = [100,870]
		self.walkCount = 0	
		self.vel = 5
		self.hitbox = (self.x , self.y, 1, 1)
		self.health = 20 
		self.visible = True 



	def hit(self):
		if self.health > 0:
			self.health -= 2
		elif self.health == 0:
			self.visible = False			
			score = 0			
			score += 5


	def draw(self, win):
		self.move()
		if self.visible:		
			if self.walkCount + 1 >= 33: # Since we have 11 images for each animtion our upper bound is 33. 
                                 # We will show each image for 3 frames. 3 x 11 = 33.
				self.walkCount = 0
        
		if self.vel > 0: # If we are moving to the right we will display our walkRight images
			win.blit(self.walkRight[self.walkCount// 3], (self.x,self.y))
			self.walkCount += 1
		else:  # Otherwise we will display the walkLeft images
			win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
			self.walkCount += 1
		pygame.draw.rect(win, (60, 63, 60), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) 
		pygame.draw.rect(win, (111,210,46), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10)) # NEW
		self.hitbox = (self.x + 50 , self.y , 18 , 57)

    # update this sprite's position
	def update(self):
    # if it goes off the bottom of the screen, "kill" it, which will remove
    # it from any group of sprites that it is in
		if self.health == 0 :
			self.kill(self)
			self.isvisible = False


	# Goes inside the enemy class
	def move(self):
		if self.vel > 0: 
			if self.x < self.path[1] + self.vel: 
				self.x += self.vel
			else: 
				self.vel = self.vel * -1
				self.x += self.vel
				self.walkCount = 0
		else: #if we are moving left
			if self.x > self.path[0] - self.vel: 
				self.x += self.vel
			else: #change our direction
				self.vel = self.vel * -1
				self.x += self.vel
				self.walkCount = 0
		

	
