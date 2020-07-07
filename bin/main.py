

import pygame
from pygame.locals import *
import sys

from core.first_eye import Screen_Manager
from core.handler import Manager
from core.sort_score import Score_Manager

def main():
    pygame.init()
    pygame.font.init()
    mr = Screen_Manager()
    mg = Manager()
    ms = Score_Manager()


    while 1:
        mg.judge_time()              # 判断游戏超时

        if mr.status == 0:           # 游戏未开始状态
            mr.open_game_init()

        if mg.status == 1:           # 游戏正在进行状态
            mg.reset_animal()        # 随机分配元素
            AnimalSpriteGroup = mg.start_game_init()
            mg.clear_ele()    # 标记清除
            mg.is_death_map() # 死图判断
            mg.exchange_ele(AnimalSpriteGroup)  # 元素交换
        mg.stop_game()               # 结束游戏

        if ms.status == 2:           # 游戏排行榜状态
            mg.record_score()        # 记录本场游戏得分， 并分数清零
            ms.choice_game_init()

        for event in pygame.event.get():
            # 退出游戏事件的判断

            if event.type == KEYDOWN:
                if event.key == K_q or event.key == K_ESCAPE:
                    sys.exit()
            if event.type == QUIT:
                sys.exit()

            mg.mouse_select(event)      # 对游戏进行中的事件监听
            # 注意两个事件监听的顺序不可调换,  避免点击 "开始游戏" 的鼠标事 对 mg.cur_sel 进行赋值
            # 使 Base.status = 1 的赋值在程序最后
            ms.mouse_select(event)
            mr.mouse_select(event)      # 对游戏首屏的事件监听


        # mg.mouse_image()  # 更换鼠标图片， 但使得程序变得很重， 需要考虑

