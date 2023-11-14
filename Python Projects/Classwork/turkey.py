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

    screen.fill((255, 0, 255))

    pygame.draw.circle(screen, (0, 0, 0), (500, 550), 50)
    pygame.draw.circle(screen, (100, 150, 255), (475, 600), 50)
    pygame.draw.circle(screen, (50, 90, 255), (550, 525), 50)

    pygame.draw.ellipse(screen, (110, 70, 0),
                        (WIDTH // 2, HEIGHT // 2, 250, 300))
    pygame.draw.ellipse(screen, (255, 70, 0), (560, 400, 125, 200))

    pygame.draw.circle(screen, (255, 255, 255), (600, 475), 25)
    pygame.draw.circle(screen, (255, 255, 255), (650, 475), 25)
    pygame.draw.circle(screen, (0, 0, 0), (600, 475), 15)
    pygame.draw.circle(screen, (0, 0, 0), (650, 475), 15)

    pygame.display.flip()

pygame.quit()
