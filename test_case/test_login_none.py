#-*- coding: utf-8 -*-
def test_login_none(self):
		try:
			self.browser.find_element_by_class_name('login_none').click()
			print "click login button."
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)