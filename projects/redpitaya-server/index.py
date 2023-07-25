from http.server import SimpleHTTPRequestHandler, HTTPServer
from utils import getParams
from commands import blink
from response import rJSON, rHTML, div, rFile

PORT = 1337

class RedPitayaHandler(SimpleHTTPRequestHandler):
    def log_request(self, code='-', size='-'):
        return # disable logging
    def log_message(self, format, *args):
        return # disable logging

    def do_GET(self):
        print("Sending", self.path)
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
            print("No such path")
            return rHTML(self, "<h1>404 Not Found</h1>", 404)


def serve(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Serving at port", port)
    httpd.serve_forever()

def serve_loop(port):
    port = int(port)
    try:
        serve(port)
    except OSError:
        serve_loop(port+1)

if __name__ == "__main__":
    print("Starting RedPitaya Server on port", PORT)

    try:
        serve_loop(PORT)
    except KeyboardInterrupt:
        print("Stopping RedPitaya Server")
        exit(0)
    except Exception as e:
        print("Error:", e)
        exit(1)