import pygame

from .base import Base
from .entity import Element
from .handler import Manager


class Screen_Manager(Base):
    """
    游戏 首屏 的 管理
    """

    def __init__(self):
        super(Screen_Manager, self).__init__()

    def open_game_init(self):
        """ 游戏 首屏 页面 初始化 """
        # if self.status == 0:
        # 绘制 首屏的 背景 图片
        Element(Element.bg_open_image, (0, 0)).draw(self.screen)
        # 开始 按钮 的 绘制
        Element(Element.game_start_button_image, Element.game_start_button_posi).draw(self.screen)
        pygame.display.flip()

    def mouse_select(self, event):
        """ 游戏 首屏 事件 监听  """
        if self.status == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # 开始 游戏 按钮  监听
                if Element.game_start_button_posi[0] < mouse_x < Element.game_start_button_posi[0] + \
                        Element.start_button[0] \
                        and Element.game_start_button_posi[1] < mouse_y < Element.game_start_button_posi[1] + \
                        Element.start_button[1]:
                    Base.status = 1
                    Manager.start_time = pygame.time.get_ticks()  # 初始化 游戏的 开始时间




