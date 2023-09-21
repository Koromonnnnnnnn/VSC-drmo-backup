import pygame

pygame.init()


#creates game screen and caption
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Pong")

#game variables
doExit = False #variable to quit out of game loop

clock = pygame.time.Clock()

p1x = 20
p1y = 200

p2x = 660
p2y = 200

bx = 350
by = 250

bVx = 5
bVy = 5

#BEGIN GAME LOOP######################################################
while not doExit:
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1y-=5
    if keys[pygame.K_s]:
        p1y+=5
    
    keys2 = pygame.key.get_pressed()
    if keys2[pygame.K_UP]:
        p2y-=5
    if keys2[pygame.K_DOWN]:
        p2y+=5

    bx += bVx
    by += bVy

    if bx < 0 or bx + 20 > 700:
        bVx *= -1
    if by < 0 or by + 20 > 700:
        bVy *= -1

    #render section-----------------------------------
    screen.fill((0,0,0)) #wipe the screen black
    
    pygame.draw.line(screen, (255, 255, 255), [349, 0], [349,500], 5)

    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100), 1)

    pygame.draw.rect(screen, (255, 255, 255), (p2x, p2y, 20, 100), 1)

    pygame.draw.circle(screen, (244, 244, 244), (bVx, bVy), 50)

    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()