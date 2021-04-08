from wsgiref.simple_server import make_server
import falcon

class PongResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = ('pong')

app = falcon.App()

app.add_route('/ping', PongResource())

if __name__ == '__main__':
    with make_server('', 80, app) as httpd:
        print('Serving on port 80...')

        httpd.serve_forever()
