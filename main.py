import asyncio

from database import create_tables_and_db


async def main():
    print("Hello from job-application-tracker!")
    await create_tables_and_db()


if __name__ == "__main__":
    asyncio.run(main())
