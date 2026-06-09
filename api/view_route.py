from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from application_repository import ApplicationRepository
from core.database import get_db
from core.template import templates
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
