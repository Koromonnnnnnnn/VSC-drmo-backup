import pygame
import math
import random

pygame.init()


# creates game screen and caption
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Slither")
clock = pygame.time.Clock()

# game variables
doExit = False  # variable to quit out of game loop

xPos = 200
yPos = 200
Vx = 1
Vy = 1

# classes are like a template that you build and then use to stamp out lots of copies of a particular object.


class pellet:
    def __init__(self, xPos, yPos, red, green, blue, radius):
        self.xPos = xPos
        self.yPos = yPos
        self.red = red
        self.green = green
        self.blue = blue
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen, (self.red, self.green,
                                    self.blue), (self.xPos, self.yPos), self.radius)
# end class pellet

# p1 = pellet(200, 50, 100, 20, 220, 10)
# p2 = pellet(120, 250, 0 , 180, 90, 30) #(position, position, color, color, color, size)
# p3 = pellet(50, 200, 0, 0, 0, 50)


pelletBag = list()

for i in range(10):
    pelletBag.append(pellet(random.randrange(0, 400), random.randrange(0, 400), random.randrange(0, 255), random.randrange(
        # randomizes x,y values and puts the pellets randomly on the screen
        0, 255), random.randrange(0, 255), 10))


# BEGIN GAME LOOP######################################################
while not doExit:

    # pygame's way of listening for events (key presses, mouse clicks, etc)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True  # lets you quit program

    # keyboard input-----------------------------------

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos

        if mousePos[0] > xPos:
            Vx = 1
        else:
            Vx = -1
        if mousePos[1] > yPos:
            Vy = 1
        else:
            Vy = -1

    # Physics

    xPos += Vx
    yPos += Vy
    # render section-----------------------------------

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (200, 0, 200), (xPos, yPos), 12)

    for i in range(10):
        pelletBag[i].draw()

    pygame.display.flip()  # update graphics each game loop

# END GAME LOOP#######################################################
pygame.quit()
