import tornado.ioloop
import tornado.web
import tornado.escape
from Party import *

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

class HostPartyHandler(tornado.web.RequestHandler):

    def post(self):
        print(self.request.body)

class JoinPartyHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Join PARTY!!")

class CommandHandler(tornado.web.RequestHandler):

    def post(self):
        cmd_json = tornado.escape.json_decode(self.request.body)
        func_name = cmd_json["command"]
        params = cmd_json["params"]

        #execvute command 
        assert hasattr(Party,func_name), "invalid command"
        print(getattr(Party,func_name)(*params))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/hostparty", HostPartyHandler),
        (r"/joinparty", JoinPartyHandler),
        (r"/command", CommandHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()