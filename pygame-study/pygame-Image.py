import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./image/background.png")
screen.blit(bg, (0, 0))


# 绘制英雄
hero = pygame.image.load("./image/hero1.png")
screen.blit(hero, (150, 500))

pygame.display.update()


while True:
    pass

pygame.quit()