import pygame

pygame.init()


# creates game screen and caption
pygame.display.set_caption("flowers!")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0, 0, 0))  # paint background black

RED = (250, 0, 0)
ORANGE = (200, 100, 0)
GREEN = (0, 150, 0)

# Flower 1
# (190, 330) is my top left corner
pygame.draw.rect(screen, (GREEN), (290, 220, 20, 100))
pygame.draw.circle(screen, (RED), (280, 220), 20)
pygame.draw.circle(screen, (RED), (280, 180), 20)
pygame.draw.circle(screen, (RED), (320, 220), 20)
pygame.draw.circle(screen, (RED), (320, 180), 20)
pygame.draw.circle(screen, (ORANGE), (300, 200), 20)

# Flower 2
# (190, 330) is my top left corner
pygame.draw.rect(screen, (RED), (190, 330, 20, 100))
pygame.draw.circle(screen, (GREEN), (180, 330), 20)
pygame.draw.circle(screen, (GREEN), (180, 290), 20)
pygame.draw.circle(screen, (GREEN), (220, 330), 20)
pygame.draw.circle(screen, (GREEN), (220, 290), 20)
pygame.draw.circle(screen, (255, 255, 255), (200, 310), 20)

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
pygame.quit()  # pygame flowers!
