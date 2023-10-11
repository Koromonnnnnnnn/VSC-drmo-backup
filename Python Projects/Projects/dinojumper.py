import pygame

pygame.init()


# creates game screen and caption
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("dino jumper")

# game variables
doExit = False  # variable to quit out of game loop
clock = pygame.time.Clock()


# BEGIN GAME LOOP######################################################
while not doExit:

    # pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True  # lets you quit program

    # timer
    clock.tick(60)

    # keyboard input-----------------------------------

    # render section-----------------------------------

    pygame.display.flip()  # update graphics each game loop

# END GAME LOOP#######################################################
pygame.quit()
