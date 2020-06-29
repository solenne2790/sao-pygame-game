import pygame
pygame.init()
import sys     
import os 


from player import Player
from enemy import Enemy
from game import Game


win = pygame.display.set_mode((1080,720))
bg = pygame.image.load("background.png")
pygame.display.set_caption("First Game")


clock = pygame.time.Clock()

#pygame.mixer.music.load("music.wav")
#pygame.mixer.music.play(1)
score = 0


def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (255,255,255))    
    win.blit(text, (950, 10))	
    kirito.draw(win)
    golem.draw(win)

    
    pygame.display.update()


#mainloop
font = pygame.font.SysFont('comicsans', 30 ,True)
score_actuel = 0

kirito = Player(800,600)
golem = Enemy(600,100 )

run = True
while run:

     
    clock.tick(22)
    keys = pygame.key.get_pressed()

    

    if kirito.hitbox[1] < golem.hitbox[1] + golem.hitbox[3] and kirito.hitbox[1] + kirito.hitbox[3] > golem.hitbox[1]:
        if kirito.hitbox[0] + kirito.hitbox[2] > golem.hitbox[0] + golem.hitbox[2]: 
            kirito.hurt()            
            score -= 5    


    if keys[pygame.K_SPACE]: 
        kirito.attack = True




    if keys[pygame.K_LEFT] and kirito.x > kirito.vel:
        kirito.x -= kirito.vel
        kirito.left = True
        kirito.right = False
        kirito.standing = False
    elif keys[pygame.K_RIGHT] and kirito.x < 1080 - kirito.width - kirito.vel:
        kirito.x += kirito.vel
        kirito.right = True
        kirito.left = False
        kirito.standing = False
    else:
        kirito.standing = True
        kirito.walkCount = 0
        
    if not(kirito.isJump):
        if keys[pygame.K_UP]:
            kirito.isJump = True
            kirito.right = False
            kirito.left = False
            kirito.walkCount = 0
    else:
        if kirito.jumpCount >= -10:
            neg = 1
            if kirito.jumpCount < 0:
                neg = -1
            kirito.y -= (kirito.jumpCount ** 2) * 0.5 * neg
            kirito.jumpCount -= 1
        else:
            kirito.isJump = False
            kirito.jumpCount = 10
            


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        

    redrawGameWindow()



pygame.quit()







