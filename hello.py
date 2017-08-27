import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        # self.write("Hello, world")
        self.render("index.html")


# class ChatHandler():

#     def foo(self):
#         pass


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8085)
    tornado.ioloop.IOLoop.current().start()
