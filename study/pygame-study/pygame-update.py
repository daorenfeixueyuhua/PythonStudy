import pygame

# 初始化
pygame.init()

# 创建游戏窗口 大小 480 * 700
screen = pygame.display.set_mode((480,700))
# 绘制图像

# 1> 加载图像数据
bg = pygame.image.load("./image/background.png")

# 2> 绘制图像
screen.blit(bg,(0,0))

# 3> update 更新屏幕显示
# pygame.display.update()

# 绘制英雄
hero = pygame.image.load("./image/hero1.png")
screen.blit(hero, (100,500))
pygame.display.update()


while True:
    pass

# 结束
pygame.quit()
