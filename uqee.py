#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner
#import Image, ImageEnhance, ImageFilter
#from pytesser import *

class Uqee(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(30)
		self.base_url = "http://www.uqee.com"
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_login(self):
		username = 'nocooldown'
		passwd = '111111'
		self.browser.get(self.base_url + "/")
		try:
			self.browser.find_element_by_link_text('登录').click()
			self.browser.find_element_by_id('username').send_keys(username)
			self.browser.find_element_by_id('userpw').send_keys(passwd)
			self.browser.find_element_by_class_name('login_btn').click()
			print "click login button."
		except:
			print "element not finded yet."
			browser.get_screenshot_as_file("D:\msysgit\msysgit\git\selenium_test\log_err.png")
			time.sleep(2)	
	'''def Image(self):
		threshold = 140
		table = []
		for i in range(256):
			if i < threshold:
				table.append(0)
			else:
				table.append(1)
		rep = {'o':'0', 'I':'1', 'L':'1', 'Z':'2', 'S':'8'}
		#open the image
		im = Image.open(name)
		#change to lightness
		imagry = im.convert('L')
		imagry.save('g' + name)
		#
		out = imagry.point(table, '1')
		out.save('b' + name)
		#recognition
		text = image_to_string(out)
		#diff recognition
		text = text.strip()
		text = text.upper()

		for r in rep:
			text = text.replace(r, rep[r])
		print text
		return text

	getverify1('v1.jpg')
	getverify1('v2.jpg')
	getverify1('v3.jpg')
	getverify1('v4.jpg')
	'''
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
		self.browser.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(Uqee("test_login"))

	#rep = file('D:\msysgit\msysgit\git\selenium_test\log.html', 'wb')
	#runner = HTMLTestRunner.HTMLTestRunner(stream=rep, title='Report_title', description='Report_description')

	#runner = unittest.TextTestRunner()
	results = unittest.TextTestRunner().run(suite)	























