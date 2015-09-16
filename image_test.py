#-*- coding= utf-8 -*
import Image
import ImageFilter
#read the image
#choose the delay of longest PIL,obtain every PIL duration information,and the max is the goal
Duration = 1000
#open the image
def open_pic():
	try:
		ima = Image.open("/root/guang/selenium_test/u=2123615555,1127201059&fm=56.jpg")
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
	return imag
	ima.show()
	ima.save("ima_black.gif", "GIF")
	
#division ima
def division():
	try:
		font = []
		for i in xrange(4):
			x=7+i*13
			y=3
			font.append(img.crop((x,y,x+9,y+13)))
		return font
	except Exception,e:
		print "division failed..."

#recoginize
def recognize(ima):
    try:
        fontMods = []
        for i in range(10):
            fontMods.append((str(i), Image.open("./num/%d.bmp" % i)))
            result = ""
            font = division(imag)
            for i in font:
                target = i
                points = []
                for mod in fontMods:
                    diffs = 0
                    for yi in range(13):
                        for xi in range(9):
                            if mod[1].getpixel((xi, yi)) != target.getpixel((xi, yi)):
                                diffs += 1
                        points.append((diffs, mod[0]))
	            points.sort()
	            result += points[0][1]
            return result

if __name__ == "__main__":
    open_pic()
    binaryzation()
    division()
    recognize()

