

import sys
import pygame

from .base import Base
from .entity import Font_Fact, Element
from .handler import Manager


class Score_Manager(Base):
    """
    游戏排行榜界面的管理
    """

    def __init__(self):
        super(Score_Manager, self).__init__()

    def choice_game_init(self):
        """ 游戏排行榜界面的初始化 """
        if self.status == 2:
            # 背景的 绘制
            Element(Element.bg_choice_image, (0, 0)).draw(self.screen)
            # 游戏分数的绘制
            # pygame.draw.rect(self.screen, (0, 0, 255), Element.score_order_rect, 2)
            for k, item in enumerate(sorted(Manager.score_list, reverse=True)[:8]):
                Font_Fact(str(item) + "  Score",(Element.score_order_rect[0] + \
                                                 50, Element.score_order_rect[1] + \
                                                 k * 50), 35, (94, 67, 10)).draw(self.screen)

            # " 再来一局" 图片的绘制
            # Element(Element.again_game_image, Element.again_game_posi).draw(self.screen)
            # "退出游戏" 图片的绘制
            # Element(Element.quit_game_image, Element.quit_game_posi).draw(self.screen)
            pygame.display.flip()

    def mouse_select(self, event):
        """ 游戏排行榜界面的事件监听 """
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.status == 2:
                # "再来一次" 的鼠标监听
                if Font_Fact.again_game_posi[0] < mouse_x < Font_Fact.again_game_posi[0] + 200 \
                        and Font_Fact.again_game_posi[1] < mouse_y < Font_Fact.again_game_posi[1] + 60:
                    # 游戏进入打怪状态
                    Base.status = 1
                    # 分数置 0
                    Manager.destory_animal_num = [0, 0, 0, 0, 0, 0]
                    # 初始化游戏开始时间
                    Manager.start_time = pygame.time.get_ticks()

                # "退出游戏" 的鼠标监听
                elif Font_Fact.quit_game_posi[0] < mouse_x < Font_Fact.quit_game_posi[0] + 200 \
                        and Font_Fact.quit_game_posi[1] < mouse_y < Font_Fact.quit_game_posi[1] + 60:
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pass