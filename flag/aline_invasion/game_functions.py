#! /usr/local/bin/python3
# -*- coding:utf8 -*-

"""
    function: 存储大量让游戏运行的函数
"""


import sys
import pygame


def check_keydown_events(event, ship): 
    """
    响应按键 
    """ 
    if event.key == pygame.K_RIGHT:
        # ship.rect.centerx += 1
        ship.moving_right = True 
    elif event.key == pygame.K_LEFT: 
        ship.moving_left = True 

def check_keyup_events(event, ship): 
    """ 
    响应松开
    """ 
    if event.type == pygame.K_RIGHT: 
        ship.moving_right = False
    elif event.type == pygame.K_LEFT: 
        slip.moving_left = False


def check_event(ship):
    """
    响应按键和鼠标事件
    :param ship: 飞船实例对象
    :return:
    """
    for event in pygame.event.get():
        # print(event)
        # print(event.type)
        # print(pygame.QUIT)
        # 当玩家单机游戏窗口的关闭按钮时, 将检测到 pygame.QUIT 事件
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # 向左移动飞船
            # check_keydown_events(event, ship)
            if event.key == pygame.K_RIGHT:
                # ship.rect.centerx += 1
                ship.moving_right = True 
            elif event.key == pygame.K_LEFT: 
                ship.moving_left = True 
            
        elif event.type == pygame.KEYUP: 
            # check_keyup_events(event, ship) 
            if event.type == pygame.K_RIGHT: 
                ship.moving_right = False
            elif event.type == pygame.K_LEFT: 
                slip.moving_left = False  


def update_screen(ai_settings, screen, ship):
    """
    更新屏幕上的图像, 并切换到新屏幕
    :param ai_settings: 初始化设置实例对象
    :param screen: 元素, 屏幕对象
    :param ship: 飞船实例对象
    :return:
    """
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见, 不断更新屏幕, 以显示元素的新位置, 并在原来的位置隐藏元素, 从而营造平滑移动的效果
    pygame.display.flip()


if __name__ == "__main__":
    pass
