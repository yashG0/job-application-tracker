from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api.application_route import application_routes

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(application_routes)

app.mount("/static", StaticFiles(directory="static"), name="static")
