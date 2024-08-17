import os
from asyncio import run

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models import Task, User


async def init():
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))

    await init_beanie(database=client.workshop, document_models=[User, Task])
    client.drop_database(name_or_database=client.workshop)
    tasks = [
        Task(name="clean floor"),
        Task(name="buy lego"),
        Task(name="sail"),
        Task(name="drink beers"),
    ]
    ids = await Task.insert_many(tasks)
    ids = ids.inserted_ids
    users = [
        User(
            name="Adam",
            surname="Brzyzek",
            email="hotbrzyzek@gmail.com",
            recently_tasks=[tasks[0], tasks[1]],
        ),
        User(
            name="Kamil",
            surname="Kulig",
            email="kamil.marek.kulig@gmail.com",
            recently_tasks=[tasks[2], tasks[3]],
        ),
    ]
    # LOOOK OUT ON TYPO IN DATA if you write task not recently tasks will not show error or any mistake
    ids = await User.insert_many(users)
    print(ids)


if __name__ == "__main__":
    run(init())
