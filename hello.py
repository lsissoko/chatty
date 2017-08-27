import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.autoreload
import os

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

        for conn in global_connections:
            conn.write_message(message)

        global_messages.append(message)

    def on_close(self):
        print("connection closing")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", ChatHandler)
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8085)

    print("\n-----\nnew app \n")

    # TODO remove in prod
    tornado.autoreload.start()
    for dir, _, files in os.walk("static"):
        [tornado.autoreload.watch(dir + "/" + f)
         for f in files if not f.startswith(".")]

    tornado.ioloop.IOLoop.current().start()
