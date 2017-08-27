#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import unittest
import HTMLTestRunner1 as HTMLTestRunner
import time
import os
import shutil
import configure
from public import logutils
log = logutils.getLogger(__name__)
casepath = './'
def Creatsuite():
	# 定义单元测试容器
	testunit = unittest.TestSuite()
	# 定搜索用例文件的方法
	discover = unittest.defaultTestLoader.discover(casepath, pattern='main*', top_level_dir=None)
	# 将测试用例加入测试容器中
	for testsuite in discover:
		for casename in testsuite:
			testunit.addTest(casename)
		print(testunit)
	return testunit


test_case = Creatsuite()
# 获取系统当前日期
day = time.strftime('%Y-%m-%d')
#定义个报告存放路径，支持相对路径
# aaa = os.path.exists('./result/' + day)
# if aaa:
# 	shutil.rmtree('./result/' + day)
# os.mkdir('./result/' + day)
# os.mkdir('./result/' + day + '/screencap')
filename = './result/' + day + '/result.html'
fp = file(filename, 'wb')

log.info('获取手机信息')
cmd = 'adb -s %s shell cat /system/build.prop>phone.txt' %configure.device_name
os.popen(cmd)
info = open('phone.txt', 'r')
lines = info.readlines()
phone_brand = ''
phone_model = ''
phone_version = ''
try:
	for i in lines:
		if 'ro.product.manufacturer' in i:
			phone_brand = i.replace('ro.product.manufacturer', '手机品牌')
		if 'ro.product.model' in i:
			phone_model = i.replace('ro.product.model', '手机型号')
		if 'ro.build.version.release' in i:
			phone_version = i.replace('ro.build.version.release', '系统版本')
except:pass
info.close()
os.remove('phone.txt')

# 定义测试报告
title=u'%s--%s测试报告(%s * %s * %s)'%(configure.game_name,configure.channel_name,phone_brand, phone_model ,phone_version)
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title , description=u'用例执行情况：')
#运行测试用例
runner.run(test_case)
fp.close()  # 关闭报告文件
#unittest.TextTestRunner(verbosity=2).run(test_case)