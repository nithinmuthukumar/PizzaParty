import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,asdfghjk):
        self.write("fjfjff")
    # def post(self, asdfghjk):
    #     print(asdfghjk)
    #     print(self.request)
    #     print(self.request.body)
    #     self.write({"fg":9})

def make_app():
    return tornado.web.Application([
        (r"/(.*)", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()