import pygame

pygame.init()

# creates game screen and caption

screen = pygame.display.set_mode((800, 800))  # create game screen
pygame.display.set_caption("A lovely House!")  # window title

pygame.draw.rect(screen, (200, 0, 200), (200, 400, 300, 300))
pygame.draw.rect(screen, (255, 255, 255), (380, 350, 100, 100))
pygame.draw.rect(screen, (255, 255, 255), (230, 350, 100, 100))
pygame.draw.rect(screen, (165, 42, 42), (300, 500, 100, 200))
pygame.draw.circle(screen, (144, 200, 0), (100, 100), 50)
pygame.draw.circle(screen, (100, 150, 0), (150, 100), 50)
pygame.draw.circle(screen, (230, 150, 0), (200, 150), 50)
pygame.draw.circle(screen, (244, 150, 0), (250, 200), 50)
pygame.draw.circle(screen, (244, 244, 244), (50, 200), 50)
pygame.draw.polygon(screen, (0, 244, 200),
                    ((200, 400), (500, 400), (400, 100)))


# game variables
doExit = False  # variable to quit out of game loop


# BEGIN GAME LOOP######################################################
while not doExit:

    # pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True  # lets you quit program

    # keyboard input-----------------------------------

    # render section-----------------------------------

    pygame.display.flip()  # update graphics each game loop

# END GAME LOOP#######################################################
pygame.quit()
