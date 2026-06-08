import uvicorn
from fastapi import FastAPI

from api.application_route import application_routes

app = FastAPI()

app.include_router(application_routes)


if __name__ == "__main__":
    uvicorn.run(app, reload=True)
