import socket
try:
	s=socket.socket()
	host=socket.gethostname()
	port=9000
	s.bind((host,port))
	s.listen(6)
	print "waiting for client request"
	#print s.accept()
	cobj,cinfo = s.accept()
	cobj.send('acknowleged successfully')
	client_data = cobj.recv(1024)
	client_data = float(client_data)
	resp = "EVEN" if client_data%2==0 else "ODD"
	cobj.send(resp)
except Exception as err:
	print err
finally:
	s.close()