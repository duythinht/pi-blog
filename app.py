#!/usr/bin/env python

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world!")

application = tornado.web.Application([
    ("/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
