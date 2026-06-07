from os import getenv

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from model import Base

load_dotenv()

DB_URL: str | None = getenv("DB_URL")

if DB_URL is None:
    raise ValueError("Database URL could'nt be loaded!")

engine = create_async_engine(
    DB_URL,
    echo=True,
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
)


async def create_tables_and_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    sess: AsyncSession = AsyncSessionLocal()
    try:
        yield sess
    finally:
        await sess.aclose()
