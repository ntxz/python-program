import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("打飞机")
    #创建一艘飞船
    ship = Ship(screen)
    #设置背景色
    bg_color = (230,230,230)
    #开始游戏主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ship)
        gf.update_screen(ai_settings,screen,ship)
                        
run_game()
        
