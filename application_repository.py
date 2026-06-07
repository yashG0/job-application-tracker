from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from model import Application, ApplicationStatus


class ApplicationRepository:
    def __init__(self, sess: AsyncSession) -> None:
        self.session: AsyncSession = sess

    async def create(self, new_application: Application) -> Application:
        self.session.add(new_application)
        await self.session.commit()
        await self.session.refresh(new_application)
        return new_application

    async def get_by_id(self, application_id: int) -> Application | None:
        return await self.session.get(Application, application_id)

    async def get_all_applications(self) -> list[Application]:
        result = await self.session.scalars(select(Application))
        return list(result)

    async def delete(self, application_id: int) -> bool:
        application_exists = await self.session.get(Application, application_id)
        if application_exists is None:
            return False
        await self.session.delete(application_exists)
        await self.session.commit()
        return True

    async def get_by_status(
        self,
        status: ApplicationStatus,
    ) -> list[Application]:
        result = await self.session.scalars(
            select(Application).where(Application.status == status)
        )

        return list(result)
