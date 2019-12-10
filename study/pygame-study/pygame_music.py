import sys, pygame
import time
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

soundObj = pygame.mixer.Sound("./music/刮风zth070528.wav")
soundObj.play(-1, 0, 0)

fontObj = pygame.font.Font("freesansbold.ttf", 32)
textSurfaceObj = fontObj.render("Music", True, BLACK, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (100, 128)

DISPLAYSURF.fill(WHITE)
DISPLAYSURF.blit(textSurfaceObj,textRectObj)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            soundObj.stop()
            pygame.quit()
            sys.exit()


    pygame.display.update()