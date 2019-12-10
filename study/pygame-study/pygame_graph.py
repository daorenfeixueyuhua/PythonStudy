import sys, pygame
from pygame.locals  import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BULE  = (  0,   0, 255)

DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((160, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BULE, (60, 60), (60, 120), 4)
pygame.draw.line(DISPLAYSURF, BULE, (120, 60), (60, 120))
pygame.draw.circle(DISPLAYSURF, RED, (100, 100), 100, 2)
pygame.draw.rect(DISPLAYSURF, RED, (0, 0, 200, 200), 1)
pygame.draw.ellipse(DISPLAYSURF, RED, (100, 100, 300, 250), 2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

pygame.quit()
