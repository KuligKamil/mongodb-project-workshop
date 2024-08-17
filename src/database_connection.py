import os

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models import Task, User


async def database_init():
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    await init_beanie(
        database=client.workshop,
        document_models=[Task, User],
        multiprocessing_mode=True,
    )
    # client.drop_database(name_or_database=client.workshop)
