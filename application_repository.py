from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from model import Application, ApplicationStatus


class ApplicationRepository:
    def __init__(self, sess: AsyncSession) -> None:
        self.session: AsyncSession = sess

    async def delete(self, app_id: int) -> bool:
        app_exists = await self.session.get(Application, app_id)
        if app_exists is None:
            return False

        await self.session.delete(app_exists)
        await self.session.commit()
        return True

    async def update_status(
        self, app_id: int, new_status: ApplicationStatus
    ) -> Application | None:
        app_exists = await self.session.get(Application, app_id)
        if app_exists is None:
            return None
        app_exists.status = new_status
        await self.session.commit()
        await self.session.refresh(app_exists)
        return app_exists

    async def create(self, new_application: Application) -> Application:
        self.session.add(new_application)
        await self.session.commit()
        await self.session.refresh(new_application)
        return new_application

    async def get_by_id(self, application_id: int) -> Application | None:
        return await self.session.get(Application, application_id)

    async def get_all(self) -> list[Application]:
        result = await self.session.scalars(
            select(Application).order_by(desc(Application.company))
        )
        return list(result)

    async def delete_app(self, application_id: int) -> bool:
        application_exists = await self.session.get(Application, application_id)
        if application_exists is None:
            return False
        await self.session.delete(application_exists)
        await self.session.commit()
        return True

    async def get_by_status(
        self,
        app_status: ApplicationStatus,
    ) -> list[Application]:
        result = await self.session.scalars(
            select(Application).where(Application.status == app_status)
        )

        return list(result)

    async def dashboard_status(self) -> list[tuple[ApplicationStatus, int]]:
        result = await self.session.execute(
            select(
                Application.status,
                func.count(Application.id),
            ).group_by(Application.status)
        )

        return [(status, count) for status, count in result]
