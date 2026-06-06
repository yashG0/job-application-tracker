from os import getenv

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

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


async def get_db():
    sess: AsyncSession = AsyncSessionLocal()
    try:
        yield sess
    finally:
        await sess.aclose()
