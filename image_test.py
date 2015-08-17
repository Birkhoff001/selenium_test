#-*- coding= utf-8 -*
import Image
import ImageFilter
#read the image
#choose the delay of longest PIL,obtain every PIL duration information,and the max is the goal
Duration = 1000
def open_pic():
	try:
		ima = Image.open(imagename)
		print ima.format, ima.size, ima.mode
	except Exception, e:
		print "load image ......failed!"
	ima.show()

def binaryzation():
	coordinate = (100, 100, 200,200)
	region = ima.crop(coordinate)
	region.show()
	#region = region.transpose(Image.ROTATE_180)     //旋转图片180°
	region.convert("RGBA")

	imafilter = ima.filter(ImageFilter.DETAIL)
	imafilter.show()
	for x in xrange(ima.size[1]):
		for y in xrange(ima.size[0]):
			if ima.load()[x,y][0] < 90):
				ima.load()[x,y] = (0,0,0,255)

	for x in xrange(ima.size[1]):
		for y in xrange(ima.size[0]):
			if ima.load()[x,y][1] < 136:
				ima.load()[x,y] = (0,0,0,255)

	for x in xrange(ima.size[1]):
		for y in xrange(ima.size[0]):
			if ima.load[x,y][2] > 0:
				ima.load[x,y] = (255,255,255,255)
	ima.show()
	ima.save(path + f)


load_ima = []
index_ima = 0
for i in range(10):
	im.seek(i)
	load_ima.append(ima.load())
	if im.info['duration'] > Duration:
		index_ima = i
load_imas = load_ima[index_ima]

#获取验证色块的代码(0-255)
#统计一帧中相同色块的出现频率按高到低排序
#把验证帧和噪音帧的频率做比较，去除相同的部分（即噪音色块）
width = 100
height = 50

d = {}
for i in xrange(width):
	for j in xrange(height):
		k = load_ima[index_ima][i, j]
		if d.has_key(k):
			d[k][0] += 1
			d[k].append((i, j))
		else:
			d[k] = [1, (i, j)]
topd = sorted(d.items(), cmp=lambda x,y:cmp(y[1][0], x[1][0]))

for i in xrange(width):
	for j in xrange(height):
		load_imas[i, j] = 0

found = 0
for (k, v) in topd:
	if not isnoise(v[1:]):
		for point in v[1:]:
			load_imas[point[0], point[1]] = k
		found += 1
	else:
		print k, 'is noise'

	if found == 4:
		break;
return load_imas

def printload_imas(load_imas, code = -1):
	for i in xrange(width):
		for j in xrange(height):
			if (code == -1 and frame[i, j] != 0) or (code != -1 and load_imas[i,j] == code):
				print '*'
			else:
				print '-'
		print

#对每一个字母进行旋转与缩放
#选择一个顶点，做射线
#找到和字母相切的两条射线
#把图像旋转射线与水平线的偏离角度(Image.rotate)
#缩放到固定大小



#把处理后字母和特征库进行比较
#用最简单的距离比较法
#特征库就多找几幅图搞定

