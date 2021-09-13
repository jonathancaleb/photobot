
import tornado.web
import tornado.ioloop

class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        files = self.request.files["imgFile"]
        for f in files:
            fh = open(f"img/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
            self.write("http://localhost:8080/img/{f.filename}")    

if (__name__ == "_main_"):
    app = tornado.web.Application([
        ("/", uploadHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler, {"path" :"img"})
    ])

    app.listen(8080)
    print("Listening on port 8080")

    tornado.ioloop.IOLoop.instance().start()


import PIL
import tornado
from PIL import Image
from tkinter.filedialog import *


file_path = askopenfilename()
img = PIL.Image.open(file_path)
myHeight, myWidth = img.size

img = img.resize((myHeight, myWidth) , PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()

img.save(save_path+"_compressed.JPG")
