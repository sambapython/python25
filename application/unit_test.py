# operation1 test casese:
"""
case1: inp: 1,2 outp=2
case2: inp: None,None outp=None
case3: inp: 2,"str1"  outp=str1str1
case4:inp:()            outp=None
"""
from app import application
import unittest

class TestApp(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.userinstance="<user123>"
		print "setupClass"
	@classmethod
	def tearDownClass(cls):
		cls.userinstance=None
		print "teardown class"

	def setUp(self):
		print self.userinstance
		print "setup excuted"
	def tearDown(self):
		print self.userinstance
		print "teardown executed"
	def test_1_2(self):
		
		print self.userinstance
		print "test_1_2"
		app1 = application(1,2)
		res=  app1.operation1()
		self.assertTrue(2==res,"1,2 input testcase failed")

	def test_None_None(self):
		print "test_None_None"
		app1 = application(None,None)
		res=  app1.operation1()
		self.assertTrue(None==res,"None,None input testcase failed")
	def test_2_str1(self):
		print "test_2_str1"
		app1 = application(2,"str1")
		res=  app1.operation1()
		self.assertTrue("str1str1"==res,"2,str1 input testcase failed")
if __name__ == "__main__":
	unittest.main()


