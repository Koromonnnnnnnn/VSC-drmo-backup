import pygame
import math

pygame.init()


#creates game screen and caption
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Slither Jaime")
clock = pygame.time.Clock()

#game variables
doExit = False #variable to quit out of game loop

xPos = 200
yPos = 200
Vx = 1
Vy = 1

#BEGIN GAME LOOP######################################################
while not doExit:
   
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
  
     
    #render section-----------------------------------
    
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (200, 0, 200), (xPos, yPos), 12)


    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()