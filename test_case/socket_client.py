#-*- coding: utf-8 -*-
import socket
import sys
import game
def socket_client(image):
	try:
		c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except Exception, e:
		print 'Failed to create socket.' + str(e)

	print 'Socket create successful-----1.'

	host = '10.0.253.149'
	port = 9118
	try:
		remote_ip = socket.gethostbyname(host)
	except Exception, e:
		print 'Hostname could not be resolved.' + str(e)

	print host + " " + remote_ip + "..."
	print "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"

	c.connect((remote_ip, port))
	print 'client connect to' + " " + host
	c.send(image)
	print 'client send send send to-----------'
	data = c.recv(1024)
	print "Reply from server------%s" %data

if __name__ == "__main__":
	socket_client(image)


