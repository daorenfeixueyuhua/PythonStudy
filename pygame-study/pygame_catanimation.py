import pygame, sys
from pygame.locals import *

pygame.init()

# frames per second setting
FPS = 30
fpsClock = pygame.time.Clock()

# set up the windows
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Animation")

WHITE = (255, 255, 255)
catImg = pygame.image.load("./image/cat.png")
catX = 10
catY = 10
direction = "right"

while True:

    DISPLAYSURF.fill(WHITE)

    if direction == "right":
        catX += 5
        if catX == 280:
            direction = "down"
    elif direction == "down":
        catY += 5
        if catY == 220:
            direction = "left"
    elif direction == "left":
        catX -= 5
        if catX == 10:
            direction = "up"
    elif direction == "up":
        catY -= 5
        if catY == 10:
            direction = "right"

    DISPLAYSURF.blit(catImg, (catX, catY))
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)