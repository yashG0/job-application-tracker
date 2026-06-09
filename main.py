from fastapi import FastAPI

from api.application_route import application_routes
from api.view_route import view_route
from core.static import static_files

app = FastAPI()

app.mount(
    "/static",
    static_files,
    name="static",
)

app.include_router(application_routes)
app.include_router(view_route)
