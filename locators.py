#-*- coding: utf-8 -*-
import unittest
#from pageobjects import locators, selenium_server_connection
#from pageobjects.basepageobject import BasePageObject
#from pageobjects.basepageelement import BasePageElement


class UsernameElement(BasePageElement):
	def __init__(self):
		self.locators = locators["login.username"]

	def __set__(self, obj, val):
		se = selenium_server_connection.connection
		se.type(self.locators, val)

class PasswordElement(BasePageElement):
	def __init__(self):
		self.locators = locators["login.password"]

	def __set__(self, obj, val):
		se = selenium_server_connection.connection
		se.type(self.locators, val)

class LoginPageObject(BasePageElement):
	username = UsernameElement()
	password = PasswordElement()

	def __init__(self, se):
		self.se = se
		self.se.open("/login")
		self.assertEqual("My Application - Login", self.se.get_tile())

	def submit(self):
		wait_for = "selenium.broserbot.getCurrentWindow().document.getElementByld('LogoutButton)"
		self.se.click(locators["login.submit"])
		self.se.wait_for_condition(wait_for, "30000")











