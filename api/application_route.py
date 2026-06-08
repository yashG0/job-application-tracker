from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from application_repository import ApplicationRepository
from database import get_db
from model import ApplicationStatus
from schema import ApplicationInSchema, ApplicationOutSchema
from services import ApplicationService

application_routes = APIRouter(prefix="/application", tags=["Application"])


@application_routes.get("")
async def get_all(sess: AsyncSession = Depends(get_db)):
    repo = ApplicationRepository(sess)
    service = ApplicationService(repo)
    return await service.get_all()


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


@application_routes.get("/status")
async def get_by_status(
    status: ApplicationStatus,
    sess: AsyncSession = Depends(get_db),
):
    repo = ApplicationRepository(sess)
    service = ApplicationService(repo)
    return await service.count_by_status(app_status=status)
