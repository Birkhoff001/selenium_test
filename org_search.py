#-*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class OrgSearch():
	def setUp(self):
		self.dr = webdriver.Firefox()

	def test_search_org(self):
		self.dr.get("http://uqee.com")

	def tearDown(self):
		self.dr.close()

if __name__ == "__main__":
	unittest.main()



