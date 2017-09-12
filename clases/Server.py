__author__ = 'GastonLucero'

import tornado.ioloop
import tornado.web
import tornado.httpserver
import os
from controllers.MainHandler import MainHandler
from controllers.ChartHandler import ChartHandler


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/chart/(?P<symbol>[^\/]+)/", ChartHandler),
            (r"/", MainHandler),
        ]
        settings = {
            "template_path": os.path.join(os.path.dirname(__file__), "..", "views"),
            "static_path": os.path.join(os.path.dirname(__file__), "..", "assets"),
            "debug": True,
        }
        tornado.web.Application.__init__(self, handlers, **settings)


class Server(object):

    def __init__(self, port):
        self.port = port
        self.host = '0.0.0.0'
        self.application = Application()
        self.http_server = tornado.httpserver.HTTPServer(self.application)

    def run_server(self):
        self.http_server.listen(self.port)
        print("Starting HTTP server on port " + str(self.port))
        tornado.ioloop.IOLoop.instance().start()
