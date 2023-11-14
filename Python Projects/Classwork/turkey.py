import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turkey!")

doExit = False


while not doExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True  # lets you quit program

    # render section-----------------------------------

    screen.fill((0, 0, 0))
    
    pygame.draw.ellipse(screen, (110, 70, 0), (WIDTH // 2, HEIGHT // 2, 200, 200))
    pygame.display.flip()

pygame.quit()
