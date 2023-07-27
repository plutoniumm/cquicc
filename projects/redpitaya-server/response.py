import json

# content type map
contentTypes = {
    "html": "text/html",
    "json": "application/json",
    "css" : "text/css",
    "js"  : "application/javascript",
    "svg" : "image/svg+xml",
    "png" : "image/png"
}

def getContentType(file):
    ext = file.split(".")[-1]
    if ext in contentTypes:
        return contentTypes[ext]
    else:
        print("Unknown content type" + ext + " for file " + file)
        return "text/plain"

def rFile(server,data,status=200,headers={}):
    server.send_response(status)
    server.send_header('Content-type', getContentType(data))
    for key in headers:
        server.send_header(key, headers[key])
    server.end_headers()

    with open(data, 'rb') as f:
        server.wfile.write(f.read())

def rJSON(server,data,status=200,headers={}):
    server.send_response(status)
    server.send_header('Content-type', 'application/json')
    for key in headers:
        server.send_header(key, headers[key])
    server.end_headers()

    server.wfile.write(json.dumps(data).encode())

def rHTML(server,data,status=200,headers={}):
    server.send_response(status)
    server.send_header('Content-type', 'text/html')
    for key in headers:
        server.send_header(key, headers[key])
    server.end_headers()

    server.wfile.write(data.encode())


def rText(server,data,status=200,headers={}):
    server.send_response(status)
    server.send_header('Content-type', 'text/plain')
    for key in headers:
        server.send_header(key, headers[key])
    server.end_headers()

    server.wfile.write(data.encode())

def div(data,style=""):
    return "<div style='" + style + "'>" + data + "</div>"