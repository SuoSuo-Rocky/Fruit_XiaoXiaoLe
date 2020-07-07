

import pygame
class Base:
    """
    一些 公共的 变量的 管理
    """

    clock = pygame.time.Clock()  # 创建一个对象来帮助跟踪时间,
    _screen_size = (900, 600)  # 屏幕 的 大小
    _cell_size = 50  # 矩阵中每个小方块 为边长为 50 的正方形
    _width = 9  # 矩阵 的 行数
    _height = 9  # 矩阵的 列数
    matrix_topleft = (250, 100)  # 矩阵的 左上顶点坐标
    status = 0  # 0: 游戏未开始， 1: 游戏正在 进行  2:游戏中间状态， 等待抉择 3. 游戏时间到

    def __init__(self):
        self.screen = pygame.display.set_mode(self._screen_size)
        pygame.display.set_caption("明日科技")
