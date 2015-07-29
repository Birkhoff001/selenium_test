#-*- coding: utf-8 -*-
def test_cooperative_account(self):
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