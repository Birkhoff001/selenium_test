#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Uqee(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(30)
		self.base_url = "http://www.uqee.com"
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_login(self):
		try:
			self.browser.find_element_by_link_text('登录').click()
			print "click login button."
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)

		self.browser.find_element_by_id('username').send_keys(username)
		self.browser.find_element_by_id('userpw').send_keys(passwd)
		self.browser.find_element_by_class_name('login_btn').click()

	
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
	unittest.main()























