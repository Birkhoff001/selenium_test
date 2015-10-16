#-*- coding= utf-8 -*-
#image_game.py
import Image
import ImageFilter
import sys
import PIL
#from socket_server import *
#read the image
#choose the delay of longest PIL,obtain every PIL duration information,and the max is the goal
HEIGHT = 100
chars = " ...',;:fdsaeJIDKADFOmM"
filename = "./333.png"
#open the image
def open_pic():
    try:
        #output = ''
        print " filename = " + filename
        imag = Image.open(filename)
        imag.load()
        imag.show()
        print "open ...open..."
        print imag.format, imag.size, imag.mode
        print "23333"
        size = getsize(image)
        image = image.resize(size)
        image = image.convert('L')
        pixs = image.load()
        for y in range(size[1]):
            for x in range(size[0]):
                output += chars[pixs[x, y]/10]
            output += '\n'
        print output

    except Exception, e:
        print "image to ascii is failed..." + str(e)

def getsize(image):
    '''calculate the target picture size'''
    s_width = image.size[0]
    s_height = image.size[1]
    t_height = HEIGHT
    t_width = (t_height*s_width)/s_height
    t_width = int(t_width * 2.3)
    t_size = (t_width, t_height)
    return t_size


#binaryzation
def binary(img):
    width = img.size[0]
    height = img.size[1]
    print "/* width:%d */" % width
    print "/* height:%d */" % height
    count = 0
    for h in range(0, height):
        for w in range(0, width):
            pixel = img.getpixel((w, h))
            for i in range(0, 3):
                count = (count + 1)%16
                if (count == 0):
                    print "0x%02x, /n"%pixel[i]
                else:
                    print "0x%02x,"%pixel[i]

def binaryzation():
    try:
        #coordinate = (100, 100, 200,200)
        #region = img.crop(coordinate)
		#region.show()
		#region = region.transpose(Image.ROTATE_180)
        #region.convert("RGBA")
        imgfilter = img.filter(ImageFilter.DETAIL)
        imgfilter.show()
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if img.load()[x,y][0] < 90:
                    img.load()[x,y] = (0,0,0,255)
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if img.load()[x,y][1] < 136:
                    img.load()[x,y] = (0,0,0,255)
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if img.load[x,y][2] > 0:
                    img.load[x,y] = (255,255,255,255)
    except Exception, e:
        print "the binaryzation failed..."
    img.show()
    img.save(".\\1113_black.gif", "GIF")
    #blow up imgge
    img_black = Image.open('.\\game_black.gif').resize((1000, 500), Image.NEAREST)
    return img_black

    print "image binaryzation success!"
if __name__ == "__main__":
    '''if len(sys.argv) < 2:
        print "Useage: pic2ascii.py filename"
        sys.exit(1)
    filename = sys.argv[1]
    '''
    open_pic()
