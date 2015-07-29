#-*- coding: utf-8 -*-
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