#!/usr/bin/env python
# coding=utf-8
import os
import unittest
import atx
from time import sleep, strftime
import public.methods as public
import configure
from public import logutils
log = logutils.getLogger(__name__)
####################
channel_pay_activity = u'com.sdk2345.pay.PayActivity'
channel_login_activity = u'com.game2345.account.SigninActivity'
channel_announcement_activity = u'com.game2345.account.floating.EventActivity'
wechat = u'com.tencent.mm'
alipay =u'com.alipay.sdk.app.H5PayActivity'
unionpay = u'com.unionpay.uppay.PayActivity'
#####################
class Channel(public.Methods):

	def input_account(self,driver):
		input1 = self.element(driver, 'className', 'android.widget.EditText')
		input1.click()
		for i in range(len(input1.text)):
			driver.adb_shell(['input', 'keyevent', '123'])
			driver.adb_shell(['input', 'keyevent', '67'])
		driver.adb_shell(['input', 'text', configure.account])
		driver.keyevent('KEYCODE_ENTER')
		for i in range(len(input1.text)):
			driver.adb_shell(['input', 'keyevent', '123'])
			driver.adb_shell(['input', 'keyevent', '67'])
		driver.adb_shell(['input', 'text', configure.password])
		driver.keyevent('KEYCODE_ENTER')
		self.element(driver, 'text', '登录').click()
		sleep(2)
		for i in xrange(5):
			if self.get_view_info(driver) == channel_login_activity:
				driver.keyevent('BACK')


	def NewUpdate_act(self, driver):
		u'''ewan更新'''
		for i in xrange(20):
			act = driver.current_app()
			if act[1] == u'cn.ewan.supersdk.activity.NewUpdateActivity':
				self.element(driver, 'className', 'android.widget.Button').click()
				log.info('点击稍后更新')
				return act[1]
			else:
				log.info('等待更新activity')
				sleep(1)
		return None


	def Notice_act(self, driver):
		u'''ewan公告'''
		for i in xrange(20):
			act = driver.current_app()
			if act[1] == u'cn.ewan.supersdk.activity.NoticeActivity':
				self.element(driver, 'className', 'android.widget.Button').click()
				log.info('点击关闭公告')
				return act[1]
			else:
				log.info('等待公告activity')
				sleep(1)
		return 'ok'


	def close_announcement(self, driver):
		u'''渠道公告'''
		for i in xrange(10):
			if self.get_view_info(driver) == channel_announcement_activity:
				self.element(driver, 'className', 'android.widget.ImageView').click()
				log.info('点击关闭渠道公告')
				return 'ok'
			else:
				log.info('渠道公告没弹出')
		return 'ok'


	def login(self, driver):
		u'''渠道login'''
		for i in xrange(20):
			if self.get_view_info(driver) == channel_login_activity:
				self.input_account(driver)
				image = self.images_or_none(driver, 'login_exist@auto.png')
				if image:
					log.info('登录成功')
					return 'ok'
				else:
					log.info('登录失败')
					return None

			else:
				image = self.images_or_none(driver, 'login_exist@auto.png')
				if image:
					log.info('自动登录成功')
					return 'ok'
				else:
					self.game_click2(driver, 'enter_game')

	def wechat(self,driver):

		if self.pay_exist_act(driver,'wechat_in',0) == wechat: #判断微信的package naem
			for i in xrange(2):
				driver.keyevent('BACK')                        # 按2次back 键
			self.pay_out(driver,'wechat_out')                  #  渠道支付界面退出
			if self.get_view_info(driver) != channel_pay_activity:  #判断是否退出成功
				return 'ok'
			else:
				return None
		else:
			return None

	def ali(self,driver):
		if self.pay_exist_act(driver,'ali_in')== alipay:
			driver.keyevent('BACK')
			self.pay_out(driver,'ali_out')
			if self.get_view_info(driver) != channel_pay_activity:
				return 'ok'
			else:
				return None
		else:
			return None


	def zhangyu(self,driver):
		if self.pay_exist_pic(driver, 'zhangyu_in'):
			driver.keyevent('BACK')
			if self.get_view_info(driver) != channel_pay_activity:
				return 'ok'
			else:
				return None
		else:
			return None

	def qq(self,driver):
		if self.pay_exist_pic(driver, 'qq_in'):
			driver.keyevent('BACK')
			if self.get_view_info(driver) != channel_pay_activity:
				return 'ok'
			else:
				return None
		else:
			return None

	def union(self,driver):
		if self.pay_exist_act(driver, 'union_in',1) == unionpay:
			driver.keyevent('BACK')
			self.element(driver,'text','确定').click()
			sleep(2)
			self.pay_out(driver, 'union_out')
			if self.get_view_info(driver) != channel_pay_activity:
				return 'ok'
			else:
				return None
		else:
			return None

	def union2(self,driver):
		if self.pay_exist_act(driver, 'union2_in',1) == unionpay:
			driver.keyevent('BACK')
			self.element(driver,'text','确定').click()
			sleep(2)
			self.pay_out(driver, 'union2_out')
			if self.get_view_info(driver) != channel_pay_activity:
				return 'ok'
			else:
				return None
		else:
			return None

	def China_Mobile(self,driver):
		if self.pay_exist_pic(driver, 'China_Mobile_in'):   # 判断第三方支付界面
			driver.keyevent('BACK')                         # 退出支付界面
			if self.get_view_info(driver) != channel_pay_activity:  #判断是否退出成功
				return 'ok'
			else:
				return None
		else:
			return None

	def China_Unicom(self,driver):
		if self.pay_exist_pic(driver, 'China_Unicom_in'):
			driver.keyevent('BACK')
			if self.get_view_info(driver) != channel_pay_activity:
				return 'ok'
			else:
				return None
		else:
			return None

	def China_Telecom(self,driver):
		if self.pay_exist_pic(driver, 'China_Telecom_in','channel','up'):
			driver.keyevent('BACK')
			if self.get_view_info(driver) != channel_pay_activity:
				return 'ok'
			else:
				return None
		else:
			return None


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(YSDKSDK)
	#suite =unittest.TestLoader().loadTestsFromName(YSDKSDK)
	unittest.TextTestRunner(verbosity=2).run(suite)
	'''now_time = strftime("%Y-%m-%d %H_%M_%S")
	filename = 'D:/test_result/'+now_time+"-result.html"
	fp = open(filename, 'wb')
	case_shuo_ming = u'测试情况'
	HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=case_shuo_ming).run(suite)
	fp.close()'''