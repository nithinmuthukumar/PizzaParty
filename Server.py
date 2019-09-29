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
        cmd_name = cmd_json["command"]
        params = cmd_json["params"]

        #execvute command
        assert hasattr(Party,cmd_name), "invalid command"
        result = getattr(Party,cmd_name)(*params) #return result to front-end


        #send function return value if it isnt null
        if result == None:
            return None

        msg = tornado.escape.json_encode({"command":cmd_name,"return_value":result})
        self.write(msg)



def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/command", CommandHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()