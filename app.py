import tornado.ioloop as ioloop
import tornado.web as web
import tornado.escape  as escape
import asyncio
import queryImagesAWS as query
import json

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class MainHandler(web.RequestHandler):

    def get(self):
        self.render("index.html")

    def post(self):
        data = json.loads(self.request.body)
        if data and data['data']:
            results = query.search(data['data'])
            respond = ''
            for r in results:
                respond += '<div class="card text-center" style="width: 18rem;"><img src="' + r['img']
                respond += '" class="card-img-top" alt="' + r['img'] + '"><h5 class="card-title">' + r['category']
                respond += '</h5></div></div>'
            self.write(respond)
        else:
            self.send_error(404)


def make_app():
    return web.Application([
        (r"/", MainHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    ioloop.IOLoop.current().start()