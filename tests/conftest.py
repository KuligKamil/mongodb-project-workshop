import os

import pytest_asyncio
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.models import Task, User


@pytest_asyncio.fixture(scope="session", autouse=True)
async def mongo_database_fixture():
    try:
        client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
        await init_beanie(
            document_models=[User, Task],
            database=client.tests,
            multiprocessing_mode=True,
        )
    except Exception as e:
        print(e)
    finally:
        client.drop_database(client.tests)
