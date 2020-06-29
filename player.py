import pygame

# on cree une premiere classe qui représente notre joueur #
pygame.init()
from enemy import Enemy
from game import Game

        
sword_sound = pygame.mixer.Sound("Sword.wav")
sword_sound.set_volume(0.6)


class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load('standing.png')
		player_sprite = pygame.sprite.Group()		
		self.health = 20
		self.hitbox = (120 , 120, 10, 10)	
		self.x = 10		
		self.y = 550		
		self.width = 116		
		self.vel = 10
		self.attack = 5
		self.attack = False		
		self.isJump = False
		self.left = False
		self.right = False
		self.walkCount = 0
		self.jumpCount = 10
		self.attackCount = 0		
		self.standing = True  
		self.visible = True		
			
#method when the character hit the golem	
	def hurt(self):
		self.health = -5		



	def Attack(self):
		self.attack = 5
		sword_sound = pygame.mixer.Sound("Sword.wav")
		sword_sound.play()


	def draw(self, win):
		if self.walkCount + 1 >= 27:
			self.walkCount = 0
		if self.attackCount + 1 >= 27:		
			self.attackCount = 0
		if not(self.standing):
			if self.left:
				win.blit(walkLeft[self.walkCount//4], (self.x,self.y))
				self.walkCount += 1
			elif self.attack:
				win.blit(attackRight[self.attackCount//4], (self.x,self.y))
				self.attackCount += 1
			
			elif self.right:
				win.blit(walkRight[self.walkCount//3], (self.x,self.y))
				self.walkCount += 1
			elif self.attack:
				win.blit(attackLeft[self.attackCount//3], (self.x,self.y))
				self.attackCount += 1
		else:
			if self.right:
				win.blit(walkRight[0], (self.x, self.y))
					

			else:
				win.blit(waiting[0], (self.x, self.y))
				self.hitbox = (self.x + 17, self.y + 11, 29, 52)
		
		pygame.draw.rect(win, (60,63,60), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) #barre supérieure
		pygame.draw.rect(win, (111,210,46), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10)) #bar inf 
		self.hitbox = (self.x + 30 , self.y - 10 , 31 , 57)
		

waiting = [pygame.image.load('W1.png'),pygame.image.load('W2.png')] 

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]


attackLeft = [ pygame.image.load('Attack_Left(1).png'),pygame.image.load('Attack_Left(2).png'), pygame.image.load('Attack_Left(3).png'),pygame.image.load('Attack_Left(4).png'), pygame.image.load('Attack_Left(5).png'), pygame.image.load('Attack_Left(6).png'), pygame.image.load('Attack_Left(7).png'), pygame.image.load('Attack_Left(8).png')]
pygame.image.load('Attack_Left(9).png') 

attackRight = [ pygame.image.load('Attack_Right(1).png'),pygame.image.load('Attack_Right(2).png'), pygame.image.load('Attack_Right(3).png'),pygame.image.load('Attack_Right(4).png'), pygame.image.load('Attack_Right(5).png'), pygame.image.load('Attack_Right(6).png'), pygame.image.load('Attack_Right(7).png'), pygame.image.load('Attack_Right(8).png'), pygame.image.load('Attack_Right(9).png')]
 
		



















