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
oldX = 200
oldY = 200
counter = 0

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

    def collide(self, x, y):
        if math.sqrt((x-self.xPos)*(x-self.xPos)+(y-self.yPos) * (y-self.yPos)) < self.radius + 6:
            self.xPos = random.randrange(0, 400)
            self.yPos = random.randrange(0, 400)
            self.red = random.randrange(0, 255)
            self.blue = random.randrange(0, 255)
            self.green = random.randrange(0, 255)
            self.radius = random.randrange(0, 30)
            return True


class tailSeg:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def update(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def draw(self):
        pygame.draw.circle(screen, (200, 0, 0), (self.xPos, self.yPos), 12)

# end class pellet

# p1 = pellet(200, 50, 100, 20, 220, 10)
# p2 = pellet(120, 250, 0 , 180, 90, 30) #(position, position, color, color, color, size)
# p3 = pellet(50, 200, 0, 0, 0, 50)


pelletBag = list()
tail = list()

for i in range(10):
    pelletBag.append(pellet(random.randrange(0, 400), random.randrange(0, 400), random.randrange(0, 255), random.randrange(
        0, 255), random.randrange(0, 255), 10))
for i in range(10):
    if pelletBag[i].collide(xPos, yPos) == True:
        tail.append(tailSeg(oldX, oldY))


# BEGIN GAME LOOP######################################################
while not doExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True  # lets you quit program

    # Counter should be inside the game loop
    counter += 1

    # Reset counter if it reaches 20
    if counter == 20:
        counter = 0
        oldX = xPos
        oldY = yPos

        if len(tail) > 2:
            for i in range(len(tail)):
                tail[len(tail) - i - 1].xPos = tail[len(tail) - i - 2].xPos
                tail[len(tail) - i - 1].yPos = tail[len(tail) - i - 2].yPos
            if len(tail) > 0:
                tail[0].update(oldX, oldY)

    # Event handling for mouse motion
    for event in pygame.event.get():
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

    xPos += Vx
    yPos += Vy
    # render section-----------------------------------

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (200, 0, 200), (xPos, yPos), 12)

    for i in range(10):
        pelletBag[i].collide(xPos, yPos)
    for i in range(10):
        pelletBag[i].draw()
    for i in range(len(tail)):
        tail[i].draw()

    pygame.display.flip()  # update graphics each game loop

# END GAME LOOP#######################################################
pygame.quit()
