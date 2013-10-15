#!/usr/bin/env python

import os
import tornado.web
import tornado.httpserver
from tornado.options import define
define("port", default=5000, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world!")

application = tornado.web.Application([
    ("/", MainHandler),
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(os.environ.get("PORT", 5000))

    # start it up
    tornado.ioloop.IOLoop.instance().start()
