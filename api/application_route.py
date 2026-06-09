from core.database import get_db
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from application_repository import ApplicationRepository

from model import ApplicationStatus
from schema import ApplicationInSchema, ApplicationOutSchema, DashboardStatsSchema
from services import ApplicationService

application_routes = APIRouter(prefix="/application", tags=["Application"])


@application_routes.get("")
async def get_all(sess: AsyncSession = Depends(get_db)):
    repo = ApplicationRepository(sess)
    service = ApplicationService(repo)
    return await service.get_all()


@application_routes.get("/status")
async def get_by_status(
    status: ApplicationStatus,
    sess: AsyncSession = Depends(get_db),
):
    repo = ApplicationRepository(sess)
    service = ApplicationService(repo)
    return await service.count_by_status(app_status=status)


@application_routes.get(
    "/dashboard", status_code=status.HTTP_200_OK, response_model=DashboardStatsSchema
)
async def get_dashboard(sess: AsyncSession = Depends(get_db)):
    repo = ApplicationRepository(sess)
    service = ApplicationService(repo)
    return await service.dashboard()


@application_routes.get(
    "/{app_id}", response_model=ApplicationOutSchema, status_code=status.HTTP_200_OK
)
async def get_by_id(app_id: int, sess: AsyncSession = Depends(get_db)):
    repo = ApplicationRepository(sess)
    service = ApplicationService(repo)
    return await service.get_by_id(app_id)


@application_routes.post(
    "/new", response_model=ApplicationOutSchema, status_code=status.HTTP_201_CREATED
)
async def create_application(
    new_app: ApplicationInSchema, sess: AsyncSession = Depends(get_db)
):
    repo = ApplicationRepository(sess)
    service = ApplicationService(repo)
    return await service.create(new_application=new_app)


@application_routes.patch(
    "/status/{app_id}",
    response_model=ApplicationOutSchema,
    status_code=status.HTTP_200_OK,
)
async def update_status(
    app_id: int, new_status: ApplicationStatus, sess: AsyncSession = Depends(get_db)
):
    repo = ApplicationRepository(sess)
    service = ApplicationService(repo)
    return await service.update_status(app_id, new_status)


@application_routes.delete("/{app_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_app(app_id: int, sess: AsyncSession = Depends(get_db)):
    repo = ApplicationRepository(sess)
    service = ApplicationService(repo)
    await service.delete_app(app_id)
