#-*- coding: utf-8 -*-
#socket_server
import socket
import sys
from image_test import *
def socket_server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception, e:
        print 'Failed to create socket.' + str(e)

    print 'Socket create successful.'

    host = '10.0.253.149'
    port = 9118

    try:
        s.bind((host, port))
    except Exception, e:
        print 'Bind failed.' + str(e)
    
    print 'Socket bind complete.'

    s.listen(10)
    print 'Socket listening...'

    try:
        conn, addr = s.accept()
    except Exception, e:
        print 'accept connect failed...' + str(e)
    print 'Connected with' + " " + str(addr[0])

image_test()

if __name__ == "__main__":
    socket_server()



