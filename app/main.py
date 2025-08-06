# app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes import generate, scan
import os

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="./templates")

app.include_router(generate.router)
# app.include_router(generate.router, prefix="/generate")
app.include_router(scan.router, prefix="/ticket") 

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})