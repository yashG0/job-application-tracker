from fastapi import HTTPException, status

from application_repository import ApplicationRepository
from model import Application, ApplicationStatus
from schema import ApplicationInSchema, ApplicationOutSchema


class ApplicationService:
    def __init__(self, app_repo: ApplicationRepository):
        self.app_repo: ApplicationRepository = app_repo

    async def create(
        self, new_application: ApplicationInSchema
    ) -> ApplicationOutSchema:

        res: Application = await self.app_repo.create(**new_application.model_dump())
        return ApplicationOutSchema.model_validate(res)

    async def get_by_id(self, application_id: int) -> ApplicationOutSchema:
        res = await self.app_repo.get_by_id(application_id)
        if res is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Application with id {application_id} not found!",
            )
        return ApplicationOutSchema.model_validate(res)

    async def get_all(self) -> list[ApplicationOutSchema]:
        applications = await self.app_repo.get_all()
        return [ApplicationOutSchema.model_validate(app) for app in applications]

    async def delete(self, app_id: int) -> None:
        is_deleted = await self.app_repo.delete(app_id)
        if not is_deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Application with id {app_id} not found!",
            )

    async def count_by_status(
        self, app_status: ApplicationStatus
    ) -> list[ApplicationOutSchema]:
        applications = await self.app_repo.get_by_status(app_status)
        return [ApplicationOutSchema.model_validate(app) for app in applications]
