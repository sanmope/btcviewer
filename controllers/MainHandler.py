__author__ = 'GastonLucero'

import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.redirect("/chart/usd/")
