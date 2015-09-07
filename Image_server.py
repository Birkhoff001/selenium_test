#-*- coding: utf-8 -*-
import StringIO
import Image, ImageDraw, ImageFont, random  
from xxx.settings import authcode_font      #请确保改字体存在
 
def make_image(request):
  mp = hashlib.md5()
  mp.update(str(datetime.datetime.now())+str(random.random()))  
  mp_src = mp.hexdigest()
  rand_str = mp_src[0:6]
  font = ImageFont.truetype(authcode_font, 25)
  width = 75
  height = 30
  im = Image.new('RGB',(width,height),'#%s'%mp_src[-7:-1])
  draw = ImageDraw.Draw(im)
  draw.line((random.randint(0,width),random.randint(0,height),random.randint(0,width),random.randint(0,height)))
  draw.line((random.randint(0,width),random.randint(0,height),random.randint(0,width),random.randint(0,height)))
  draw.line((random.randint(0,width),random.randint(0,height),random.randint(0,width),random.randint(0,height)))
  draw.line((random.randint(0,width),random.randint(0,height),random.randint(0,width),random.randint(0,height)))
  draw.line((random.randint(0,width),random.randint(0,height),random.randint(0,width),random.randint(0,height)))
  draw.text((5,2), rand_str, font=font)  
  del draw  
  buffer = StringIO.StringIO()
  im.save(buffer,'jpeg')
  httpResponse = HttpResponse(content=buffer.getvalue(),mimetype="image/jpeg")
  request.session['auth_code'] = rand_str
  return httpResponse
