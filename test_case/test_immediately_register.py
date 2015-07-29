#-*- coding: utf-8 -*-
def test_immediately_register(self):
		try:
			self.browser.find_element_by_link_text('立即注册游奇通行证').click()
			print "click login button."
		except NoSuchElementException:
			print "element not finded yet."
			time.sleep(2)