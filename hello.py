import tornado.ioloop
import tornado.web
import tornado.websocket


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")


class ChatHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        pass

    def on_message(self, message):
        self.write_message(u"Your message was: " + message)

    def on_close(self):
        pass


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", ChatHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8085)
    tornado.ioloop.IOLoop.current().start()
