#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import sleep, strftime
import public.methods as public
import configure
class Game(public.Methods):

    def enter_game(self, driver):
        '''进入游戏，有引导过引导'''
        self.game_click2(driver,'enter_game')  #点击进入游戏
        sleep(10)
        if self.guide_exist(driver,'guide_001'):  #判断是否需要过指引
            result = self.game_click(driver, 'guide')  #过指引
            return result
        else:
            result = self.game_click2(driver, 'enter_game')      #不需要过指引的操作
            return result
    def game_pay_up(self, driver):
        '''调起支付界面'''
        result = self.game_pay(driver, 'pay')
        return result

