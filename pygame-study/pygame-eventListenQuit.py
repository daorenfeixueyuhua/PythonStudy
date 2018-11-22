import pygame


# 游戏初始化
pygame.init()

screen = pygame.display.set_mode((480, 700))

# 绘制背景
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

# 游戏循环
while True:
    # 可以制定循环内部的循环频率
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():

        # 判断事件类型是否为退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")
            # 卸载所有模块
            pygame.quit()
            # 结束程序
            exit(0)

    # 2.修改飞机位置
    if hero_rect.bottom + hero_rect.height <= 0:
        hero_rect.y = 700
    hero_rect.y -= 5
    # 3.调用blit方法绘制图像
    # 解决残影
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4.调用update方法更新显示
    pygame.display.update()

pygame.quit()