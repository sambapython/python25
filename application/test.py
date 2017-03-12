# operation1 test casese:
"""
case1: inp: 1,2 outp=2
case2: inp: None,None outp=None
case3: inp: 2,"str1"  outp=str1str1
case4:inp:()            outp=None
"""
import app
# case1
app1 = app.application(1,2)
if not 2==app1.operation1():
	print "test1 failed"
else:
	print "test1pass"