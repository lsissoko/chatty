import os
from optparse import OptionParser

import tornado.autoreload
import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.websocket import WebSocketClosedError

global_connections = set()
global_messages = []


class MainHandler(tornado.web.RequestHandler):

    # TODO render global_messages as HTML
    def get(self):
        print(global_messages)
        self.render("index.html", messages=global_messages)


class ChatHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print("new connection opened")
        global_connections.add(self)

    def on_message(self, message):
        print("new message: {}".format(message))

        # TODO fix this (the error closes everyone's connection)
        # - to replicate: refresh your tab then send a message
        try:
            global_messages.append(message)
            for conn in global_connections:
                conn.write_message(message)
        except WebSocketClosedError:
            print("\nwebsocket closed when sending message\n\n")
            self.write_message("<strong style='color: red'>ERROR</strong>")

    def on_close(self):
        print("connection closing")


def make_app(debug):
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", ChatHandler)
    ], debug=debug)


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--debug", action="store_true", default=False)
    parser_options, args = parser.parse_args()

    app = make_app(parser_options.debug)
    app.listen(8085)

    print("\n-----\nnew app \n")

    if (parser_options.debug):
        tornado.autoreload.start()
        for dir, _, files in os.walk("static"):
            [tornado.autoreload.watch(dir + "/" + f)
             for f in files if not f.startswith(".")]

    tornado.ioloop.IOLoop.current().start()
