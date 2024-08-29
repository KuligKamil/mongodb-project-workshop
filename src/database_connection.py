import os

from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient


async def database_init(
    document_models: list[Document], clean_database: bool = False
) -> None:
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    await init_beanie(
        database=client.workshop,
        document_models=document_models,
        multiprocessing_mode=True,
    )
    if clean_database:
        client.drop_database(name_or_database=client.workshop)
