from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_video(
    reddit_url: str = Form(...),
    voice: str = Form(...),
    background: str = Form(...),
    captions: str = Form(...)
):
    return {
        "status": "success",
        "message": "Video generation endpoint reached successfully!"
    }
