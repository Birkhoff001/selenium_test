#-*- coding: utf-8 -*-
#socket_server
import socket
import sys
from image_game import *
import urllib
#import chardet
import struct
import binascii

def socket_server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception, e:
        print 'Failed to create socket.' + str(e)

    print 'Socket create successful-------2.'

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
        path = './image_download.png'
        conn, addr = s.accept()
        print "Server connected to %s------------" %Str(addr[0])
        data = client.recv(1024)
        print "Server receive data:%s------------" %data
        #download image
        urllib.urlretrieve(data, path)
        print "download successful......"
        Binary_change(imageName)
    except Exception, e:
        print 'download is bad!!' + str(e)
    s.close()
def Binary_change(loadImage):
    print "4444"
    binafile = str(open('loadImage', 'rb'))
    print "open binary image---------" + binafile
    binafile_ll = binafile.read()
    print "read binary image---------" + binafile_ll
    #print "read binary image---------" + binafile_ll
    image = bin(int(hexstr, 16))[2:]
    print 'bin:', image, type(image)
    print "binary successful-----------"
    #print(chardet.detect(url_image))

if __name__ == "__main__":
    socket_server()
    Binary_change()



