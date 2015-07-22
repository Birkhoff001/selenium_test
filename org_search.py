#-*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class OrgSearch(unittest.TestCase):
	def setUp(self):
		self.dr = webdriver.Firefox()
		self.dr.get("http://uqee.com")

#	def test_search_org(self):
#		main_page = page.MainPage(self.dr)
#		assert main_page.is_title_matches(), 'incorrect title matches'

	def tearDown(self):
		self.dr.close()


	#def testDefaultSize(self):
	#	assert self.widget.size() == (50, 50), 'incorrect default size'

	#def testResize(self):
	#	self.widget.resize(100, 150)
#		assert self.widget.size() == (100, 150), 'wrong size after resize'

#test suite
#	widgetTestSuite = unittest.TestSuite()
#	widgetTestSuite.addTest(WidgetTestCase("testDefaultSize"))
#	widgetTestSuite.addTest(WidgetTestCase("testResize"))

class WidgetTestSuite(unittest.TestSuite):
	def __init__(self):
		unittest.TestSuite.__init__(self,map(WidgetTestCase, ("testDefaultSize", "testResize")))
		suite = unittest.makeSuite(WidgetTestSuite, 'test')    #makesuite, and use the function sequence that test function name for init func of cmp.


	def suite():
		suite = unittest.TestSuite()
		suite.addTest(WidgetTestCase("testDefaultSize"))
		suite.addTest(WidgetTestCase("testResize"))
		return suite
		#testsuite group
		suite1 = module1.TheTestSuite()
		suite2 = module2.TheTestSuite()
		alltests = unittest.TestSuite((suite1, suite2))
		#run test and test report
		runner = unittest.TextTestRunner()
		runner.run(widgetTestSuite)





if __name__ == "__main__":
	unittest.main()



