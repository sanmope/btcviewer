__author__ = 'GastonLucero'

import tornado.web


class ChartHandler(tornado.web.RequestHandler):

    def get(self, symbol):
        if symbol in ["ltc", "usd", "eur", "ars"]:
            self._render_chart(symbol.upper())

        else:
            raise tornado.web.HTTPError(404)

    def _render_chart(self, symbol):
        self.render("stockchart.html", symbol=symbol)

