#! /usr/local/bin/python3
# -*- coding:utf8 -*-

"""
    function: 管理飞船的大部分行为
"""


import pygame


class Ship(object):

    def __init__(self, ai_settings, screen):
        """
        初始化飞船并设置其初始位置
        """
        self.screen = screen
        self.ai_settings = ai_settings 

        # 加载飞船图形并获取其外接矩形
        # linux/unix/mac
        # self.image = pygame.image.load('images\ship.jpg')
        
        # Windows 
        # self.image = pygame.image.load(r'flag\aline_invasion\images\ship.bmp')
        # Mac 
        self.image = pygame.image.load('./images/ship.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每搜新飞船放在屏幕底部中央, x轴, y轴
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性 center 中存储最小数值
        self.center = float(self.rect.centerx)

        # 移动标志 
        self.moving_right = False 
        self.moving_left = False 


    def update(self): 
        """
        根据移动标志调整飞船的位置
        """ 
        # 根据飞船的 center 值, 而不是 rect 
        # if self.moving_right: 
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            # self.rect.centerx += 1 
            self.center += self.ai_settings.ship_speed_factor 
        
        # if self.moving_left: 
        if self.moving_left and self.rect.left < 0: 
            # self.rect.centerx -= 1 
            self.center -= self.ai_settings.ship_speed_factor 

        # 根据 self.center 更新 rect 对象 
        self.rect.centerx = self.center 


    def blitme(self):
        """
        在指定位置绘制飞船
        :return:
        """
        self.screen.blit(self.image, self.rect)


if __name__ == "__main__":
    pass