import pygame


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


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


# 创建敌机精灵和精灵祖
enemy = GameSprite("./image/enemy1.png")
enemy1 = GameSprite("./image/enemy2.png", 2)
enemy_group = pygame.sprite.Group(enemy,enemy1)


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
    hero_rect.y -= 1
    # 3.调用blit方法绘制图像
    # 解决残影
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 精灵组的update和draw
    # update 组中所有精灵更新位置
    enemy_group.update()
    # draw 在screen上绘制所有精灵
    enemy_group.draw(screen)

    # 4.调用update方法更新显示
    pygame.display.update()

pygame.quit()