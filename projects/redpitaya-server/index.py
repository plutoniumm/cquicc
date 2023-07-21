from sanic import Sanic;
from sanic.response import (
  text, json, html, file_stream
);

from utils import run_scpi
from commands import blink;

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
    running, output = run_scpi()
    if not running:
      return err(output, 500);

    check = blink(2, 3);
    if not check:
      return html("<div style='color:#f22'>Couldn't Blink</div>")
    else:
      return html("<div style='color:#2f2'>Blunk LED</div>")

if __name__ == "__main__":
  print("Starting RedPitaya Server on port", PORT);

  running, output = run_scpi();
  if not running:
    print("Unable to start scpi: ", output);
    exit(1);

  app.run(
    host='0.0.0.0',
    port=PORT,
    access_log=True,
    debug=True
  );