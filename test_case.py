#-*- coding: utf-8 -*-
import os

caselist = os.listdir('D:\msysgit\msysgit\git\selenium_test\\test_case')
for case in caselist:
	exc = case.split('.')[1:][0]
	if exc == 'py':
		os.system('D:\msysgit\msysgit\git\selenium_test\\%s 1>>log.txt 2>&1' % case )
