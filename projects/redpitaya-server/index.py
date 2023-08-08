from http.server import SimpleHTTPRequestHandler, HTTPServer
from websockets import serve as wserve
import asyncio

from utils import getParams, getFile
from files import process_xy
from time import sleep
from commands import blink
from response import rHTML, div, rFile, rText, rJSON
from ws import websocket_handler

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
        elif self.path == '/ws':
            if self.headers.get('Upgrade', None) == 'websocket':
                start_server = wserve(websocket_handler, '', PORT)
                loop = asyncio.get_event_loop()
                loop.run_until_complete(start_server)
                loop.run_forever()
            else:
                return rHTML(self, "<h1>404 Not Found</h1>", 404)
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

    def do_POST(self):
        print("Receiving", self.path)
        if self.path.startswith('/plot'):
            file = getFile(self)
            png = process_xy(file)

            sleep(2)

            # base64 png
            img = "<img src='{}' alt='Matplotlib Plot'/>".format(png)

            return rHTML(self, img)


    def do_PUT(self):
        return rHTML(self, "<h1>404 Not Found</h1>", 404)
    def do_DELETE(self):
        return rHTML(self, "<h1>404 Not Found</h1>", 404)


def serve(port):
    port = int(port)

    # http server: 1337
    server_address = ('', port)
    httpd = HTTPServer(server_address, RedPitayaHandler)
    print("Serving at port", port)
    httpd.serve_forever()


if __name__ == "__main__":
    print("Starting RedPitaya Server on port", PORT)

    try:
        serve(PORT)
    except KeyboardInterrupt:
        print("Stopping RedPitaya Server")
        exit(0)
    except Exception as e:
        print("Error:", e)
        exit(1)