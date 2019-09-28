import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("lmao")
        #self.finish()
        #self.redirect()

    '''
    def post(self, msg):
        print(msg)
        print(self.request)
        print(self.request.body)
        self.write({"name":"John Dean"})
    '''

class CreatePartyHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Create PARTY!!")

class JoinPartyHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Join PARTY!!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/hostparty", CreatePartyHandler),
        (r"/joinparty", JoinPartyHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()