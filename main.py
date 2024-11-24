import pygame
from pygame.locals import *
from time import*

pygame.init
screen=pygame.display.set_mode((600,600))
player_x = 200
player_y = 200
Keys = [False, False, False, False]
player = pygame.image.load("ship.png")
background = pygame.image.load("space.jpg")

while player_y < 600:
    screen.blit(background, (0,0))
    screen.blit(player, (player_x, player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key ==K_UP:
                Keys[0]=True
            if event.key ==K_LEFT:
                Keys[1]=True
            if event.key ==K_DOWN:
                Keys[2]=True
            if event.key ==K_RIGHT:
                Keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_UP:
                Keys[0]=False
            elif event.key ==pygame.K_LEFT:
                Keys[1]=False
            elif event.key ==pygame.K_DOWN:
                Keys[2]=False
            elif event.key ==pygame.K_RIGHT:
                Keys[3]=False

    if Keys [0]:
        if player_y> 0:
            player_y -=7    
    elif Keys [2]:
        if player_y< 536:
            player_y +=7
    if Keys [1]:
         if player_> 0:
            player_x -=2
    elif Keys [3]:
         if player_x <536:
            player_x += 2

    player_y +=5
    sleep(0.05)

print("Game Over")



        
        
    


            




