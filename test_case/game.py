#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner
import socket_client
#import mdcode
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

class Game(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(30)
		self.base_url = "http://10.0.6.5/game"
		self.verificationErrors = []
		self.accept_next_alert = True
		self.browser.get(self.base_url + "/")

	def test_cookie(self):
		#self.browser.add_cookie({'name':'birkhoff', 'value':'333333'})
		for cookie in self.browser.get_cookies():
			print "%s -> %s" % (cookie['name'], cookie['value'])
			cookie = self.browser.get_cookies()
			print cookie

	def test_login(self):
		username = "allen"
		passwd = "limi"
		#identifying_code = image_game()
		#try:
		self.browser.find_element_by_id('username').send_keys(username)
		self.browser.find_element_by_id('password').send_keys(passwd)
		self.browser.find_element_by_id('codes').send_keys()
		
		try:
			print "11111111"			
			image_get = self.browser.find_element_by_xpath("//img[@id='randImage']").get_attribute("src")
			print image_get
			print "get the image."
			print(isinstance(image_get, unicode))
			print "22222222"
			time.sleep(2)
			image = image_get.encode('utf-8')
			print "encode encode---------"
			print image
			print(isinstance(image, unicode))
			print "33333333"
			#image.write(image2)
			#image.close()
#save the image
			'''image_save = open(image, 'wb').write()
			print "save save save--------------"
			image_save.flush()
			print "flush flush flush------------"
			image_save.close()'''
		except Exception, e:
			print "not found identifying code."
		print "start connect socket------------"

		socket_client.socket_client(image)
		print "send image--------"
		self.browser.find_element_by_id('rememberPswd')
		self.browser.find_element_by_xpath("//option[@value='168']").click()
		self.browser.find_element_by_class_name("linkbtn").click()

		print "click login button."
		#except:
		#	self.browser.get_screenshot_as_file("F:\selenium_test\login_err.png")
		#	print "element not finded yet."
		#	time.sleep(2)

	def test_register(self):
		try:
			self.browser.find_element_by_link_text('注册').click()
			print "click register button."		
			self.browser.find_element_by_id('username').send_keys('birkhoff')
			self.browser.find_element_by_id('userpwd').send_keys('111111')
			self.browser.find_element_by_id('userpwdok').send_keys('111111')
			self.browser.find_element_by_id('email').send_keys('123456@163.com')
			self.browser.find_element_by_id('truename').send_keys('liuyi')
			self.browser.find_element_by_id('idcard').send_keys('1234567890')
			self.browser.find_element_by_id('vdcode').send_keys()   #图形验证码
			self.browser.find_element_by_id('imageField').click()
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)

	def test_login_none(self):
		try:
			self.browser.find_element_by_class_name('login_none').click()
			print "click login button."
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)

	def test_immediately(self):
		try:
			self.browser.find_element_by_link_text('立即注册游奇通行证').click()
			print "click login button."
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)

	def test_cooperative_account(self):
		try:
			qq = self.browser.find_element_by_xpath("/Public/new/images/login_qq.jpg").click()
			weibo = self.browser.find_element_by_xpath("/Public/new/images/login_wb.jpg").click()
			renren = self.browser.find_element_by_xpath("/Public/new/images/login_rr.jpg").click()
			if (qq == 0 ):
				self.browser.find_element_by_id('switcher_plogin').click()
				self.browser.find_element_by_id('u').send_keys('123456')
				self.browser.find_element_by_id('p').send_keys('111111')
				self.browser.find_element_by_id('login_button').click()
			else:
				self.browser.find_element_by_id('rrid').send_keys('123456')
				self.browser.find_element_by_id('rrpw').send_keys('111111')
				self.browser.find_element_by_id('submit').click()
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)

	def is_alert_present(self):
		try:
			self.browser.switch_to_alert()
		except NoSuchElementException, e:
			return False
		return True

	def close_alert_and_get_its_text(self):
		try:
			alert_text = self.browser.switch_to_alert().text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text

		finally:
			self.accept_next_alert = True

	def tearDown(self):
		time.sleep(5)
		self.browser.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	#structure test suites
	suite = unittest.TestSuite()
	#suite.addTest(Game("test_cookie"))
	suite.addTest(Game("test_login"))
	#socket_client.socket_client()
	#rep = file('F:\selenium_test\log.html', 'wb')
	#runner = HTMLTestRunner.HTMLTestRunner(stream=rep, title='Report_title', description='Report_description')

#runing test
	runner = unittest.TextTestRunner()
	runner.run(suite)






























