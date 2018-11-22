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

# 1.定义rect记录飞机初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)
while True:
    # 可以制定循环内部的循环频率
    clock.tick(60)

    # 2.修改飞机位置

    hero_rect.y -= 1
    # 判断飞机位置
    if hero_rect.bottom + hero_rect.height <=0:

        hero_rect.y = 700


    # 3.调用blit方法绘制图像
    # 解决残影
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4.调用update方法更新显示
    pygame.display.update()

pygame.quit()