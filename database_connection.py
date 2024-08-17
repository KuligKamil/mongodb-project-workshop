import os

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models import Task, User


async def database_init():
    client = AsyncIOMotorClient(os.getenv("CONNECTION_STRING"))
    await init_beanie(
        database=client.workshop,
        document_models=[Task, User],
        multiprocessing_mode=True,
    )
