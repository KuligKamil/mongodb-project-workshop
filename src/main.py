from asyncio import run

from database_connection import database_init
from models import Task, User


async def init():
    await database_init(document_models=[User, Task], clean_database=True)
    users = [
        User(
            name="Adam",
            surname="Brzyzek",
            email="hotbrzyzek@gmail.com",
            recently_tasks=[],
        ),
        User(
            name="Kamil",
            surname="Kulig",
            email="kamil.marek.kulig@gmail.com",
            recently_tasks=[],
        ),
    ]
    # LOOOK OUT ON TYPO IN DATA if you write task not recently tasks will not show error or any mistake
    user_ids = await User.insert_many(users)
    # show different option how to insert
    # what return insert & why we use inserted_ids
    tasks = [
        Task(name="clean floor", user=user_ids.inserted_ids[0]),
        Task(name="buy lego", user=user_ids.inserted_ids[0]),
        Task(name="sail", user=user_ids.inserted_ids[1]),
        Task(name="drink beers", user=user_ids.inserted_ids[1]),
    ]
    ids = await Task.insert_many(tasks)
    ids = ids.inserted_ids
    user: User = await User.get(document_id=user_ids.inserted_ids[0])
    user.recently_tasks.append(tasks[0])
    user.recently_tasks.append(tasks[1])
    await user.save()
    # await User.replace()
    # tasks[0], tasks[1]
    print(ids)
    # IF YOU learn database you need to have some scale


if __name__ == "__main__":
    run(init())
