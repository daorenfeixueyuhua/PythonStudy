import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧律
FRAME_PRE_SEC = 60


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


class Backgroud(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1.调用父类的方法
        super(Backgroud, self).__init__("./image/background.png")
        # 2.判断是否是交替图像
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类的方法实现
        super(Backgroud, self).update()
        # 2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

    def __create_sprites(self):

        # 创建背景精灵和背景精灵组
        bg1 = Backgroud()
        bg2 = Backgroud(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        pass

    def start_game(self):
        print("游戏开始...")

        while True:
            # 1.设置刷新帧律
            self.clock.tick(FRAME_PRE_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collied()
            # 4.更新/绘图精灵组
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()
            pass

    def __event_handler(self):

        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collied(self):
        pass

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

    # 定义静态方法
    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()