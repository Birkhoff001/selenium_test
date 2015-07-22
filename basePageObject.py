#-*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.common.exception import NoSuchElementException
import os
import time

username = 'nocooldown'
passwd = '111111'
class instanced_selenium:
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.maximize_window()
		self.browser.set_window_size(600, 800)
		self.browser.get("http://uqee.com")

	def cookie(self):
		self.browser.add_cookie({'name':'birkhoff', 'value':'333333'})
		for cookie in browser.get_cookies():
			print "%s" -> "%s" % (cookie['name'], cookie['value'])
			cookie = browser.get_cookies()
			print cookie

	def login(self):
		try:
			self.browser.find_element_by_link_text('登录').click()
			print "click login button."
			break;
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)

		self.browser.find_element_by_id('username').send_keys(username)
		self.browser.find_element_by_id('userpw').send_keys(passwd)
		self.browser.find_element_by_class_name('login_btn').click()

	def register(self):
		try:
			self.browser.find_element_by_link_text('注册').click()
			print "click register button."
			break;
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)
		self.browser.find_element_by_id('username').send_keys('birkhoff')
		self.browser.find_element_by_id('userpwd').send_keys('111111')
		self.browser.find_element_by_id('userpwdok').send_keys('111111')
		self.browser.find_element_by_id('email').send_keys('123456@163.com')
		self.browser.find_element_by_id('truename').send_keys('liuyi')
		self.browser.find_element_by_id('idcard').send_keys('1234567890')
		self.browser.find_element_by_id('vdcode').send_keys()




	def actions_test(self):
		pass


	def teardown(self):
		self.browser.close()






