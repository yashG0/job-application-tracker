from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from application_repository import ApplicationRepository
from core.database import get_db
from core.template import templates
from model import ApplicationStatus
from services import ApplicationService

view_route = APIRouter(prefix="/pages", tags=["Pages"])


@view_route.get("/dashboard")
async def dashboard(request: Request, sess: AsyncSession = Depends(get_db)):
    app_repo = ApplicationRepository(sess)
    app_service = ApplicationService(app_repo)
    stats = await app_service.dashboard()
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"stats": stats},
    )


@view_route.get("/applications")
async def applications(request: Request, sess: AsyncSession = Depends(get_db)):
    app_repo = ApplicationRepository(sess)
    app_service = ApplicationService(app_repo)
    applications = await app_service.get_all()
    return templates.TemplateResponse(
        request=request,
        name="applications.html",
        context={"applications": applications},
    )


@view_route.get("/application/{app_id}")
async def get_application_by_id(
    app_id: int, request: Request, sess: AsyncSession = Depends(get_db)
):
    app_repo = ApplicationRepository(sess)
    app_service = ApplicationService(app_repo)
    application = await app_service.get_by_id(app_id)
    return templates.TemplateResponse(
        request=request,
        name="application_detail.html",
        context={"application": application},
    )


@view_route.get("/applications/filter/{status}")
async def filter_applications(
    status: str,
    request: Request,
    sess: AsyncSession = Depends(get_db),
):
    app_repo = ApplicationRepository(sess)
    app_service = ApplicationService(app_repo)

    if status == "all":
        applications = await app_service.get_all()
    else:
        applications = await app_service.count_by_status(ApplicationStatus[status])

    return templates.TemplateResponse(
        request=request,
        name="partials/application_list.html",
        context={
            "applications": applications,
        },
    )
