import pygame

class Ship():
    def __init__(self, ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('/home/colby/work/python_project/alien_invasion/images/ship4.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞机放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
            if self.rect.centerx == self.screen_rect.right:
                self.center = self.screen_rect.left
        elif self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
            if self.rect.centerx == self.screen_rect.left:
                self.center = self.screen_rect.right
        # 更新位置
        self.rect.centerx = self.center
        

    def blitme(self):
        """在制定位置绘制飞机"""
        self.screen.blit(self.image, self.rect)