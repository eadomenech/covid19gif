from fastapi import BackgroundTasks, FastAPI, Request
from fastapi.staticfiles import StaticFiles

from tasks import build

app = FastAPI()
app.mount("/download", StaticFiles(directory="download"), name="download")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/build")
async def build_gifs():
    build.delay()
    return {"message": "Hello World"}

@app.get('/download/<path:filename>')
async def download(filename):
    return StaticFiles('download/confirmed.gif')
