import subprocess;
from sanic import Sanic;
from sanic.response import (
  text, json, html, file_stream
);

from utils import cli;
from commands import blink, ind;

PORT=1337;

app = Sanic("redpitaya");

app.static("/", "./index.html");
app.static("/assets", "./assets", name="assets");

def err(text: str, code: int=500):
  return json({"error": text}, code);

@app.get("/get")
async def index(request):
    return html("<h1>RedPitaya Server</h1>");

@app.get("/blink")
async def blink_led(request):
    # (waits, loops)
    check = blink(2, 3);
    if not check:
      return html("<div style='color:#f22'>Couldn't Blink</div>")
    else:
      return html("<div style='color:#2f2'>Blunk LED</div>")

@app.head("/scpi")
async def scpi(request):
    running = ind();
    if not running:
      return err("SCPI server is not running", 400);
    else:
      return json({"status": "running"});


@app.post("/rce")
async def rce(request):
    # data = request.json
    data = request.body.decode();

    if not data:
        return err("Got no cmd");

    success, output = cli(data);
    if not success:
        return err(output);
    else:
        return json({"result": output});

if __name__ == "__main__":
  print(f"Starting RedPitaya Server on port {PORT}");
  app.run(
    host='0.0.0.0',
    port=PORT,
    access_log=True,
    debug=True
  );