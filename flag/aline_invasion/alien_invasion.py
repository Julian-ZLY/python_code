#! /usr/local/bin/python3
# -*- coding:utf8 -*-

"""
    function: 创建 pygame 窗口以及响应用户输入
"""


import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """
        初始化游戏并创建一个屏幕对象
    :return: None
    """

    pygame.init()
    # 调用设置类
    ai_settings = Settings()

    # screen 是一个 surface, surface 是屏幕的一部分, 用户显示游戏元素, 例如: 飞船/外星人
    # screen = pygame.display.set_mode((1000, 700))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Aline Invasion')

    # 设置背景颜色
    # bg_color = (230, 230, 230)
    # bg_color = (135, 206, 250)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)


    # 开始游戏的主循环
    while True:

        gf.check_event(ship)

        # # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     # print(event)
        #     # print(event.type)
        #     # print(pygame.QUIT)
        #     # 当玩家单机游戏窗口的关闭按钮时, 将检测到 pygame.QUIT 事件
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        ship.update() 

        gf.update_screen(ai_settings, screen, ship)
        # # 每次循环时都会重绘屏幕
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        #
        # # 让最近绘制的屏幕可见, 不断更新屏幕, 以显示元素的新位置, 并在原来的位置隐藏元素, 从而营造平滑移动的效果
        # pygame.display.flip()


if __name__ == '__main__':
    run_game()
