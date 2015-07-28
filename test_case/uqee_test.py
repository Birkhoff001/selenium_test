# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import time

username = 'nocooldown'
passwd = '111111'

class Uqee:
	def  __init__(self):
		self.browser = webdriver.Firefox()
		self.browser.set_window_size(600, 800)
		self.browser.get("http://uqee.com")
		while True:
			try:
				self.browser.find_element_by_link_text('登录').click()
				print "click login button."
				break;
			except NoSuchElementException:
				print "element not loaded yet."
				time.sleep(2)

	def cookie(self):
		self.browser.add_cookie({'name':'birkhoff', 'value':'111111'})
		for cookie in browser.get_cookies():
			print "%s -> %s" % (cookie['name'], cookie['value'])
			cookie = browser.get_cookies()
			print cookie

	def login(self):
		self.browser.find_element_by_id('username').send_keys(username)
		self.browser.find_element_by_id('userpwd').send_keys(passwd)
		self.browser.find_element_by_class_name('login_btn').click()

	

def main():
	uqee = Uqee() 
	uqee.login()

if __name__ == "__main__":
	main()






