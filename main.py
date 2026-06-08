from fastapi import FastAPI

from api.application_route import application_routes

app = FastAPI()

app.include_router(application_routes)
