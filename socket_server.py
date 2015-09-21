#-*- coding: utf-8 -*-
#socket_server
import socket
import sys
from image_game import *
import urllib
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

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
        localDir = './'
        imageName = 'image_download.jpg'
        loadImage = localDir + imageName
        conn, addr = s.accept()
        print "Server connected to %s------------" %str(addr[0])
        data = client.recv(1024)
        print "Server receive data:%s------------" %data
#download image
        urllib.urlretrieve(url, loadImage)
        print "downloading..."
    except Exception, e:
        print 'download is bad!!' + str(e)
        client.send()
        client.close()


if __name__ == "__main__":
    socket_server()



