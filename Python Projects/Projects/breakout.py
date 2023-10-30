import pygame
import math
import random

pygame.init()

screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

doExit = False

class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100, 250), random.randrange(100, 250), random.randrange(100, 250))
        self.isDead = False
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 100, 50))
    
b1 = brick(50, 50)

while not doExit:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
            
    # keyboard input-----------------------------------

    # render section-----------------------------------
    
    b1.draw()
    
    pygame.display.flip()
            
pygame.quit()
