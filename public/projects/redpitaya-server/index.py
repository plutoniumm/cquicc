from sanic import Sanic
from sanic.response import text, json

app = Sanic("redpitaya")

@app.get("/")
async def index(request):
    return text("Hello, world.")