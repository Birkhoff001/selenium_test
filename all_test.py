#-*- coding: utf-8 -*-
import unittest
import sys, re, os, math
sys.path.append("D:\msysgit\msysgit\git\selenium_test\\test_case")
#from suite import * 
from test_case import *
import uqee, test_register
import HTMLTestRunner

alltestnames = ['test_case.uqee.Uqee', 'test_case.test_register.test_register']
suite = unittest.TestSuite()

if __name__ == '__main__':
	for test in alltestnames:
		try:
			suite.addTest(unittest.defaultTestLoader.loadTestsFormName(test))
		except Exception, e:
			print 'ERROR:Skipping tests from "%s".' % test
			try:
				__import__(test)
			except ImportError:
				print 'Could not import the test module.'
			else:
				print 'Could not import the test suite.'
			from traceback import print_exc
			print_exc()


suite = unittest.Suite()
suite.addTest(unittest.makeSuite(uqee.Uqee))
suite.addTest(unittest.makeSuite(uqee_register.Uqee))


rep = file('D:\\report.html')
runner = HTMLTestRunner.HTMLTestRunner(stream=rep, title='Report_title', description='Report_description')
runner.run(suite)
#unittest.TextTestRunner(verbosity=2).run(suite)

