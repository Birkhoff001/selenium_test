#-*- coding: utf-8 -*-
import time
import tempfile
import Image

class AsciiImageProcessHandler(tornado.web.RequestHandler):
    def post(self):
        if self.request.files:
            for f in self.request.files['image']:
                rawname = f['filename']
                dstname = str(int(time.time())) + '.' +rawname.split('.').pop()
                thbname = "thumb_" + dstname

                self.write(dstname)
                tf = tempfile.NamedTemporaryFile()
                tf.write(f['body'])
                tf.seek(0)

                #create normal file
                img = Image.open(tf.name)
                img.thumbnail((920, 920), resample = 1)
                img.save("./asciiimg/" + dstname)

                #create thumb file
                img.thumbnail((100, 100), resample = 1)
                img.save("./asciiimg_tn/" + thbname)

                tf.close()


if __name__ == "__main__":
    unittest.main()


