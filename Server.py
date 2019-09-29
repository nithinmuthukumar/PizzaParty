import tornado.ioloop
import tornado.web
import tornado.escape
from Party import *

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("lmao")
        #self.finish()
        #self.redirect()

class CommandHandler(tornado.web.RequestHandler):

    def post(self):
        cmd_json = tornado.escape.json_decode(self.request.body)
        func_name = cmd_json["command"]
        params = cmd_json["params"]

        #execvute command
        assert hasattr(Party,func_name), "invalid command"
        getattr(Party,func_name)(*params) #return result to front-end

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/command", CommandHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()