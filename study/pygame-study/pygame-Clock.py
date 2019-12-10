import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./image/background.png")
screen.blit(bg, (0, 0))


# 绘制英雄
hero = pygame.image.load("./image/hero1.png")
screen.blit(hero, (150, 500))

pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

i =0

while True:
    # 可以制定循环内部的循环频率
    clock.tick(1)
    print(i)
    i += 1

pygame.quit()