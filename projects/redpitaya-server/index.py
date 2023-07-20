import subprocess;
from sanic import Sanic;
from sanic.response import (
  text, json, html, file_stream
);

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
    # (waits, loops)
    check = blink(2, 5);
    if not check:
      return html("<div style='color:red'>Couldn't Blink</div>")
    else:
      return html("<div style='color:green'>Blunk LED</div>")


@app.post("/rce")
async def rce(request):
    # data = request.json
    data = request.body.decode();

    if not data:
        return err("Got no cmd");

    try:
       print(f"Executing command: {data}")
       result = subprocess.Popen(
          data,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          shell=True,
          text=True,
          universal_newlines=True
        );
       out, error = result.communicate();

       if result.returncode != 0:
          return err(error);
       else:
          return json({"result": out});

    except subprocess.CalledProcessError as e:
        print("EXPLOSIONN")
        return err(e.stderr);


if __name__ == "__main__":
  print(f"Starting RedPitaya Server on port {PORT}");
  app.run(
    host='0.0.0.0',
    port=PORT,
    access_log=True,
    debug=True
  );