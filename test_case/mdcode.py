#-*- coding: utf-8 -*-
def mdcode(str, encoding = 'utf-8'):
	if isinstance(str, unicode):
		return str.encode(encoding)

	for c in ('utf-8', 'gbk', 'gb2312' ,'gb18030', 'utf-16'):
		try:
			if encoding == 'unicode':
				return str.decode(c)
			else:
				return str.decode(c).encode(encoding)
		except:
			pass
	raise 'Unkown charset'