#-*- coding: utf-8 -*-
import socket
import sys
def socket_client():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except Exception, e:
		print 'Failed to create socket.' + str(e)

	print 'Socket create successful.'

	host = '10.0.253.149'
	port = 9118
	try:
		remote_ip = socket.gethostbyname(host)
	except Exception, e:
		print 'Hostname could not be resolved.' + str(e)

	print host + " " + remote_ip + "..."

	s.connect((remote_ip, port))
	print 'Socket connect to' + " " + host

	message = " "

if __name__ == "__main__":
	socket_client()


