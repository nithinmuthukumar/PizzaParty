import tornado.ioloop
import tornado.web
import tornado.escape

my_url = "https://www.tornadoweb.org/en/stable/escape.html"
print(tornado.escape.url_escape((my_url)))
