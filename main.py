from asyncio import run

from beanie import Document

from src.database_connection import database_init


class User(Document):
    name: str
    surname: str
    email: str


async def main():
    await database_init(document_models=[User], clean_database=True)
    hot_adam = User(name="Adam", surname="Brzyzek", email="hotadam@gmail.com")
    await User.insert(hot_adam)


run(main())
