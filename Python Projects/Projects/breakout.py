import pygame
import math
import random

pygame.init()

screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

doExit = False

p1x = 20
p1y = 200

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
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        p1x += 5
    if keys[pygame.K_a]:
        p1x -= 5


    # render section-----------------------------------
    
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100), 20)
    
    b1.draw()
    
    pygame.display.flip()
            
pygame.quit()
