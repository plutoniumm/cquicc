import os
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
    data = request.body.decode()

    if not data:
        return json(
          {"error": "No command provided"},
          status_code=400
        )

    try:
        print(f"Executing command: {data}")
        result = os.system(data)
        return json(
          {"result": result},
          status_code=200
        )
    except Exception as e:
        return json(
          {"error": str(e)},
          status_code=500
        )

if __name__ == "__main__":
  print(f"Starting RedPitaya Server on port {PORT}");
  app.run(
    host='0.0.0.0',
    port=PORT,
    access_log=False
  );