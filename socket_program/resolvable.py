# whether perticualr server ip and port is resolvable or not...
host="www.google.com"
#port=80
#port = 800
port=443
import socket
try:
	s=socket.socket()
	s.connect((host,port))
	print "connected successfully"
except Exception as err:
	print err
finally:
	s.close()



