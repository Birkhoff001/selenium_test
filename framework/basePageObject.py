#-*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import time


class instanced_selenium:
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.maximize_window()
		self.browser.set_window_size(600, 800)
		self.browser.get("http://uqee.com")

	def cookie(self):
		self.browser.add_cookie({'name':'birkhoff', 'value':'333333'})
		for cookie in browser.get_cookies():
			print "%s -> %s" % (cookie['name'], cookie['value'])
			cookie = browser.get_cookies()
			print cookie

	username = 'nocooldown'
	passwd = '111111'
	def login(self):
		try:
			self.browser.find_element_by_link_text('登录').click()
			print "click login button."
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)

		self.browser.find_element_by_id('username').send_keys(username)
		self.browser.find_element_by_id('userpw').send_keys(passwd)
		self.browser.find_element_by_class_name('login_btn').click()

	def login_none(self):
		try:
			self.browser.find_element_by_class_name('login_none').click()
			print "click login button."
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)
	def immediately(self):
		try:
			self.browser.find_element_by_link_text('立即注册游奇通行证').click()
			print "click login button."
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)
	def cooperative_account(self):
		try:
			qq = self.browser.find_element_by_xpath("/Public/new/images/login_qq.jpg").click()
			weibo = self.browser.find_element_by_xpath("/Public/new/images/login_wb.jpg").click()
			renren = self.browse.find_element_by_xpath("/Public/new/images/login_rr.jpg").click()
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

	def register(self):
		try:
			self.browser.find_element_by_link_text('注册').click()
			print "click register button."
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)
		self.browser.find_element_by_id('username').send_keys('birkhoff')
		self.browser.find_element_by_id('userpwd').send_keys('111111')
		self.browser.find_element_by_id('userpwdok').send_keys('111111')
		self.browser.find_element_by_id('email').send_keys('123456@163.com')
		self.browser.find_element_by_id('truename').send_keys('liuyi')
		self.browser.find_element_by_id('idcard').send_keys('1234567890')
		self.browser.find_element_by_id('vdcode').send_keys()   #图形验证码
		self.browser.find_element_by_id('imageField').click()

	def actions_test(self):
		pass


	def tearDown(self):
		self.browser.close()


if __name__ ==  "__main__":
	unittest.main()





