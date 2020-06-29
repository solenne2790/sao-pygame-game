#from player import Player
from enemy import Enemy

import pygame
import random



#on crée une seconde classe qui va representer notre jeux
class Game:
	
	def __init__(self):
		#check if the game is started or not
		self.is_playing = False
		self.all_players.add(self.player)
		#generer notre joueur
		self.all_players = pygame.sprite.Group()		
		self.all_players.add(self.player)
		self.player = Player(self)
		
	
		
		self.all_enemies = pygame.sprite.Group
		self.all_enemies = pygame.sprite.Group()
		self.pressed = {}

		
	def check_collision(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, 	pygame.sprite.collide_mask)



	def update(self, win):
		# appliquer l'image du personnage
		win.blit(self.player.image, self.player.rect)

		# Actualiser la barre du joueur
		self.player.update_health_bar(screen)


