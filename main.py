#!/usr/bin/env pn
# coding=utf-8
import os
import unittest
import atx
from time import sleep, strftime
import configure
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)
class Test(unittest.TestCase,public.Methods):

	def setUp(self):

		if configure.device_name == '':
			self.driver = atx.connect()
		else:
			self.driver = atx.connect(configure.device_name)
		self.driver.start_app(configure.package_name,configure.activity_name)
		log.info('测试开始')

	def get_names(self,name):
		'''
		动态import 游戏和渠道相应的测试类
		:param name: 动态import 游戏还是 渠道
		:return: 返回 游戏 或者 渠道 实例 的类
		'''
		import public.get_names as get_names
		get_names = get_names.Get_name()
		if name =='game':
			game = __import__(get_names.get_game())
			game_name = get_names.get_game().split('.')[1]
			game = getattr(game, game_name)
			game = game.Game()
			return game
		if name == 'channel':
			channel = __import__(get_names.get_channel())
			channel_name = get_names.get_channel().split('.')[1]
			channel = getattr(channel, channel_name)
			channel = channel.Channel()
			return channel



	def tearDown(self):
		pass
		#self.driver.stop_app(configure.package_name)
		log.info('测试结束')
	def test(self):
		game = self.get_names('game')
		channel = self.get_names('channel')
		self.dy_IsNotNone(self.driver,channel.NewUpdate_act(self.driver),'NewUpdate_act')
		self.dy_IsNotNone(self.driver, channel.Notice_act(self.driver), 'Notice_act')
		self.dy_IsNotNone(self.driver, channel.close_announcement(self.driver), 'close_announcement')
		self.dy_IsNotNone(self.driver, channel.login(self.driver), 'login')
		self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'enter_game')
		for i in xrange(1,10):
			self.dy_IsNotNone(self.driver, game.game_pay_up(self.driver), 'game_pay_up')
			if i == 1:
				self.dy_IsNotNone(self.driver, channel.wechat(self.driver), 'wechat')
			elif i == 2:
				self.dy_IsNotNone(self.driver, channel.ali(self.driver), 'ali')
			elif i == 3:
				self.dy_IsNotNone(self.driver, channel.zhangyu(self.driver), 'zhangyu')
			elif i == 4 :
				pass
				#self.dy_IsNotNone(self.driver, channel.qq(self.driver), 'qq')
			elif i == 5 :
				self.dy_IsNotNone(self.driver, channel.union(self.driver), 'union')
			elif i == 6 :
				self.dy_IsNotNone(self.driver, channel.union2(self.driver), 'union2')
			elif i == 7 :
				self.dy_IsNotNone(self.driver, channel.China_Mobile(self.driver), 'China_Mobile')
			elif i == 8 :
				self.dy_IsNotNone(self.driver, channel.China_Unicom(self.driver), 'China_Unicom')
			else:
				self.dy_IsNotNone(self.driver, channel.China_Telecom(self.driver), 'China_Telecom')

if __name__ == '__main__':
	unittest.main()
