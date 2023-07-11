from sanic import Sanic
from sanic.response import (
  text, json, html, file_stream
);

PORT=1337;

app = Sanic("redpitaya");

app.static("/", "./index.html");
app.static("/assets", "./assets", name="assets");

@app.get("/get")
async def index(request):
    return html("<h1>RedPitaya Server</h1>");

if __name__ == "__main__":
  print(f"Starting RedPitaya Server on port {PORT}");
  app.run(
    host='0.0.0.0',
    port=PORT,
    access_log=False
  );