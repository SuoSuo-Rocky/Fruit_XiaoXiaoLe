

import pygame


class Element(pygame.sprite.Sprite):
    """
    绘制 图片 类
    """
    bg_open_image = "static/img/tree.png"
    bg_choice_image = "static/img/bs.png"
    bg_start_image = "static/img/bg.png"
    game_start_button_image = "static/img/game_start_button.png"
    game_start_button_posi = (300, 250)  # 开始 游戏按钮 的 坐标
    start_button = (300, 120)  # 开始 游戏按钮 的 大小
    speed = [0, 0]
    stop = 'static/img/exit.png'  # 暂停键
    stop_position = (20, 530)  # 暂停键 坐标
    frame_image = "static/img/frame.png"  # 选中框

    board_score = "static/img/task.png"  # 分数板子
    score_posi = (736, 15)  # 显示 分数 板子 的 坐标
    brick = 'static/img/brick.png'  # cell的 背景
    # 图标元组，包括6个小动物，
    animal = ('static/img/lemon.png', 'static/img/watermelon.png', 'static/img/Grapefruit.png', \
              'static/img/Kiwifruit.png', 'static/img/Nettedmelon.png', 'static/img/Avocado.png')
    # 消除 动画 图片
    bling = ("static/img/bling1.png", "static/img/bling2.png", "static/img/bling3.png", \
             "static/img/bling4.png", "static/img/bling5.png", "static/img/bling6.png", \
             "static/img/bling7.png", "static/img/bling8.png", "static/img/bling9.png")
    single_score = ('static/img/good.png', 'static/img/great.png', 'static/img/amazing.png', \
                    'static/img/excellent.png', 'static/img/unbelievable.png')
    # 0 - 9 数字 图片
    score = ('static/img/0.png', 'static/img/1.png', 'static/img/2.png', \
             'static/img/3.png', 'static/img/4.png', 'static/img/5.png', \
             'static/img/6.png', 'static/img/7.png', 'static/img/8.png', 'static/img/9.png',)
    none_animal = 'static/img/noneanimal.png'  # 无可消除小动物
    none_animal_posi = (230, 150)  # 无可 消除 动物 表示 的 坐标
    destory_animal_num = [0, 0, 0, 0, 0, 0]  # 消除各小动物的个数
    mouse_replace_image = 'static/img/mouse.png'

    count_down_image = "static/img/timeout.png"  # 游戏倒计时 图片
    count_down_posi = (35, 15)

    again_game_image = "static/img/again_game.png"  # 再来一次  的 图片
    again_game_posi = (650, 150)

    quit_game_image = "static/img/quit_game.png"  # 退出 游戏的  图片
    quit_game_posi = (650, 400)

    time_is_over_image = "static/img/time_is_over.png"  # 游戏时间 的 图片
    time_is_over_posi = (233, 50)

    startest_image = "static/img/startest.png"  # 星星 的 图片
    startest_posi = [[180 + 100, 260], [180 + 200, 260], [180 + 300, 260]]

    score_order_rect = (320, 125, 230, 400)  # 积分 排行榜 的 rect

    def __init__(self, image_file, posi):
        super(Element, self).__init__()  # 万万 不可 忘写 了， 否则 精灵 组 不管用
        self.image = pygame.image.load(image_file).convert_alpha()  # 不可是 convert()  方法 ，不理解
        self.rect = self.image.get_rect()
        self.rect.topleft = posi  # 左上角坐标
        self.speed = [0, 0]
        self.init_position = posi

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, speed):
        # 加快移动速度
        if speed[1] == 1:
            speed[1] += 1
        elif speed[0] == 1:
            speed[0] += 1
        elif speed[0] == -1:
            speed[0] += -1
        self.speed = speed
        self.rect.move_ip(*self.speed)
        if self.speed[0] != 0:  # 如果左右移动
            if abs(self.rect.left - self.init_position[0]) - 1 == self.rect[2]:  # 意味 左右 相邻 移动的 距离 正好为一个 cell 的宽度，
                self.init_position = self.rect.topleft
                self.speed = [0, 0]  #
        else:  # 上下 移动
            if abs(self.rect.top - self.init_position[1]) - 1 == self.rect[3]:  # 意味 上下相邻
                self.init_position = self.rect.topleft
                self.speed = [0, 0]


class Font_Fact(pygame.sprite.Sprite):
    """ 绘制 文字 精灵 组件 类 """

    again_game_font = "再来一局"
    again_game_posi = (620, 160)  # "再来一局" 文本位置

    quit_game_font = "退出游戏"
    quit_game_posi = (620, 400)   # "退出游戏" 文本位置

    show_time_posi = (59, 46)    # 倒计时 时间文本 位置

    def __init__(self, text, posi, txt_size=13, txt_color=(255, 255, 255)):
        self.posi = posi
        self.font = pygame.font.Font("static/font/zhengqingke.ttf", txt_size)
        self.font = self.font.render(text, False, txt_color)
        self.rect = self.font.get_rect()
        self.rect.topleft = posi

    def draw(self, screen):
        """ 绘制 方法 """
        screen.blit(self.font, self.rect)
        # 万万 不可 再次 再 pygame.display.update()  ,
        # 必须保证 每一次页面的 绘制在 最后只能有一次 pygame.display.update() 或 pygame.display.flip()
        # 否则， 当 页面 中 既有 图片的 绘制 又有 文本 的 绘制 时， 页面 中 的 图片 会出现闪烁的情况。
        # 而 页面中 全是 图片的 绘制时， 则可以忽略此情况，
        # 综上， 好习惯为： 规定每一张 页面的绘制 只在最后 有一个 pygame.displau.flip()
        # pygame.display.update()

class PlaySound(pygame.sprite.Sprite):
    """ 音频  播放类 """

    def __init__(self):
        pass
