#-*- coding: utf-8 -*-
import socket
import sys
import game
def socket_client(image):
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
	print "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"

	s.connect((remote_ip, port))
	print 'Socket connect to' + " " + host
	s.send(image)
	data = s.recv(1024)
	print "Reply from server------%s" %data

if __name__ == "__main__":
	socket_client()


