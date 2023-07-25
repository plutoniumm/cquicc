import http.server
from utils import getParams
from commands import blink
from response import rJSON, rHTML, div, rFile

PORT = 1337

class RedPitayaHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return
    def do_GET(self):
        print("GET", self.path)
        if self.path == '/':
            return rHTML(self, open('index.html').read())
        elif self.path.startswith('/assets/'):
            file = self.path[1:]
            return rFile(self, file)
        elif self.path.startswith('/blink'):
            try:
                params = getParams(self.path)
                led = int(params.get('led', 1))
                check = blink(2, 3, led)

                response = div("Couldn't Blink","color:#f22") if not check else div("Blunk","color:#2f2")

                return rHTML(self, div(response))
            except Exception as e:
                return rHTML(self, div("Couldn't Blink","color:#f22"))
        else:
            return rHTML(self, "<h1>404 Not Found</h1>", 404)


def serve(port):
    with http.server.HTTPServer(("", port), RedPitayaHandler) as httpd:
        print("Serving at port", port)
        httpd.serve_forever()

if __name__ == "__main__":
    print("Starting RedPitaya Server on port", PORT)

    try:
        serve(PORT)
    except KeyboardInterrupt:
        print("Stopping RedPitaya Server")
        exit(0)