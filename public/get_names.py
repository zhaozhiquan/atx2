#!/usr/bin/env python
#coding=utf-8
import  configure
from public import logutils
log = logutils.getLogger(__name__)
class Get_name(object):
    '''
    根据configure 配置的游戏名和渠道名，返回包含上一层级的路径
    为动态 import 提供 str
    '''
    def get_game(self):
        if configure.game_name =='hhw':
            return 'game.hhw'
        elif configure.game_name == '':
            return 'game.xx'
        else:
            log.info('该游戏没有脚本')
            exit()
    def get_channel(self):
        if configure.channel_name == 'sdk2345':
            return 'channel.sdk2345'
        elif configure.channel_name == '':
            return 'channel.xx'
        else:
            log.info('该渠道没有脚本')
            exit()