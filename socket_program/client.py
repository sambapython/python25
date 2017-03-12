import socket
try:
	s=socket.socket()
	host = socket.gethostname()
	port=9000
	s.connect((host,port))
	#print "connected successfully"
	ack = s.recv(1024)
	print ack
	#s.send('20')
	data  =raw_input("enter number:")
	s.send(data)
	resp = s.recv(1024)
	print "response from service: ",resp
except Exception as err:
	print err
finally:
	s.close()