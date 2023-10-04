import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("simple base code")

img = pygame.image.load("penguin.png").convert()
img.set_colorkey((255,0,255))

img2 = pygame.image.load("therock2.png").convert()
img2.set_colorkey((255,0,255))

doExit = False

while not doExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True 

    screen.blit(img, (200, 200))
    screen.blit(img, (random.randrange(-100, 500), 200))
    screen.blit(img2, (200, 200))
    screen.blit(img2, (random.randrange(-150, 400), 200))
    pygame.time.wait(500)
    pygame.display.flip()
  
pygame.quit()