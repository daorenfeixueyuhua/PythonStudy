import sys, pygame
from pygame.locals import *

pygame.init()
DISPLAYESURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('hello World')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()