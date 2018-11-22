import sys, pygame
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World")

WHITE = (255, 255, 255)
BULE = (0, 0, 128)
GREEN = (0, 255, 0)

fontObj = pygame.font.Font("freesansbold.ttf", 32)
textSurfaceObj = fontObj.render("hello wolrd", True, GREEN, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()