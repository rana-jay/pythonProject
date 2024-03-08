# importing the main event loop
import tornado.ioloop

# for HTTP request handlers -> to map request to request handler
import tornado.web


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello Jay')


class PostHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hi Jayyyyy </h1>")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class WeatherHandler(tornado.web.RequestHandler):
    def get(self):
        degree = int(self.get_argument("degree"))
        output = "HOT" if degree > 20 else "COLD"
        drink = "colddrinks" if degree > 20 else "Chaii"
        self.render("weather.html", output=output, drink=drink)



def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler),
        (r"/p", PostHandler),
        (r"/home", IndexHandler),
        (r"/weather", WeatherHandler),
    ],
        debug=True,
        autoreload=True
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print(f'Server is listing on port 8888')
    tornado.ioloop.IOLoop.current().start()
