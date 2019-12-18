#! /usr/local/bin/python3
# -*- coding:utf8 -*-


class Settings():
    """
    存储《外星人入侵》的所有设置的类
    """

    def __init__(self):
        """
        初始化游戏的设置
        """
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = (233, 233, 239)
        # self.bg_color = (169,169,169)

        # 飞船的设置速度 
        self.ship_speed_factor = 1.5 


if __name__ == '__main__':
    pass