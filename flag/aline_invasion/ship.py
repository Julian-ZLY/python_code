#! /usr/local/bin/python3
# -*- coding:utf8 -*-

"""
    function: 管理飞船的大部分行为
"""


import pygame


class Ship(object):

    def __init__(self, screen):
        """
        初始化飞船并设置其初始位置
        """
        self.screen = screen

        # 加载飞船图形并获取其外接矩形
        # linux/unix/mac
        # self.image = pygame.image.load('images\ship.jpg')
        
        # windows 
        self.image = pygame.image.load(r'flag\aline_invasion\images\ship.bmp')
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每搜新飞船放在屏幕底部中央, x轴, y轴
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """
        在指定位置绘制飞船
        :return:
        """
        self.screen.blit(self.image, self.rect)


if __name__ == "__main__":
    pass