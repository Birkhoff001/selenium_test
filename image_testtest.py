#-*- coding= utf-8 -*
#imgge_test.py
import Image
import ImageFilter
#read the imgge
#choose the delay of longest PIL,obtain every PIL duration information,and the max is the goal
Duration = 1000
#open the imgge
def open_pic():
	try:
		img = Image.open(img)
		print img.format, img.size, img.mode
	except Exception, e:
		print "load imgge ......failed!"
	img.show()
#binaryzation
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
	img_black = Image.open('.\\1113_black.gif').resize((1000, 500), Image.NEAREST)
	return img_black

	print "imgge binaryzation success!"

def division():
    try:
        font = []
        for i in xrange(4):
            x=7+i*13
            y=3
            font.append(img.crop((x, y, x+9, y+13)))
        return font
    except Exception, e:
        print "division failed..."

def recognize(img):
    try:
        fontMods = []
        for i in range(10):
            fontMods.append((str(i), Image.open("./num/%d.bmp" % i)))
            result = ""
            font = division(img)
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
    imgge_test()
    

