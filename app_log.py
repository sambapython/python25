import logging
logging.basicConfig(filename="log1.txt",format="%(asctime)s->%(levelname)s->%(message)s", level=logging.DEBUG)
a=raw_input("enter data:")
logging.info("a={0}".format(a))
if not a.isdigit():
	logging.warn("May get exception for the value: {0}".format(a))

try:
	res=10/float(a)
	logging.debug("res={0}".format(res)) 
except Exception as err:
	logging.exception(str(err))