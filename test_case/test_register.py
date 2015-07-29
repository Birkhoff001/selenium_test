#-*- coding: utf-8 -*-
def test_register(self):
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