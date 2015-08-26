#-*- coding= utf-8 -*
import Image
import ImageFilter
#read the image
#choose the delay of longest PIL,obtain every PIL duration information,and the max is the goal
Duration = 1000
#open the image
def open_pic():
	try:
		ima = Image.open("D:\msysgit\msysgit\git\selenium_test\\1113.jpg")
		print ima.format, ima.size, ima.mode
	except Exception, e:
		print "load image ......failed!"
	ima.show()
#binaryzation
def binaryzation():
	try:
		#coordinate = (100, 100, 200,200)
		#region = ima.crop(coordinate)
		#region.show()
		#region = region.transpose(Image.ROTATE_180)     //旋转图片180°
		#region.convert("RGBA")

		imafilter = ima.filter(ImageFilter.DETAIL)
		imafilter.show()
		for y in xrange(ima.size[1]):
			for x in xrange(ima.size[0]):
				if ima.load()[x,y][0] < 90:
					ima.load()[x,y] = (0,0,0,255)

		for y in xrange(ima.size[1]):
			for x in xrange(ima.size[0]):
				if ima.load()[x,y][1] < 136:
					ima.load()[x,y] = (0,0,0,255)

		for y in xrange(ima.size[1]):
			for x in xrange(ima.size[0]):
				if ima.load[x,y][2] > 0:
					ima.load[x,y] = (255,255,255,255)

	except Exception, e:
		print "the binaryzation failed..."
	ima.show()
	ima.save("D:\msysgit\msysgit\git\selenium_test\\1113_black.gif", "GIF")
	#blow up image
	ima_black = Image.open('D:\msysgit\msysgit\git\selenium_test\\1113_black.gif').resize((1000, 500), Image.NEAREST)
	return ima_black
	print "image binaryzation success!"



