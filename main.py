from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{folder}/{id}", response_class=HTMLResponse)
async def read_item(request: Request, folder: int, id: int):
    return FileResponse(f"static/{folder}/{id}.html")