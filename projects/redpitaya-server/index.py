import subprocess
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


@app.post("/rce")
async def rce(request):
    # data = request.json
    data = request.body.decode()

    if not data:
        return json(
          {"error": "No command provided"},
          status=400
        )

    try:
       print(f"Executing command: {data}")
       result = subprocess.Popen(
          data,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          shell=True,
          text=True,
          universal_newlines=True
        )
       out, err = result.communicate()

       if result.returncode != 0:
          return json(
            {"error": result.stderr},
            status=400
          )
       else:
          return json(
            {"result": result.stdout},
            status=200
          )

    except subprocess.CalledProcessError as e:
        print("EXPLOSIOSOSKJWSNSNNNNNNN")
        return json(
          {"error": e.stderr},
          status=400
        )


if __name__ == "__main__":
  print(f"Starting RedPitaya Server on port {PORT}");
  app.run(
    host='0.0.0.0',
    port=PORT,
    access_log=True,
    debug=True
  );