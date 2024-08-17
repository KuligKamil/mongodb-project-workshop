from asyncio import run
from collections.abc import Generator

from beanie.operators import In
from faker.factory import Factory
from faker.generator import Generator as FakerGenerator

from database_connection import database_init
from models import Address, PriorityType, SizeType, Task, User


async def main():
    await database_init()
    Faker = Factory.create
    fake = Faker(locale="pl_PL")
    fake.seed(2137)

    tasks = list(task_generator(fake=fake, number_of_iterations=100))
    tasks = await Task.insert_many(tasks)
    tasks = await Task.find_many(
        In(Task.id, tasks.inserted_ids),
    ).to_list()

    users = list(user_generator(fake=fake, tasks=tasks, number_of_tasks=3))
    await User.insert_many(users)


def task_generator(fake: FakerGenerator, number_of_iterations: int) -> Generator[Task]:
    for _ in range(number_of_iterations):
        yield Task(
            name=fake.pystr(prefix="task_", max_chars=10),
            description=fake.pystr(prefix="description_", max_chars=10),
            priority=fake.enum(PriorityType),
            size=fake.enum(SizeType),
        )


def user_generator(
    fake: FakerGenerator, tasks: list[Task], number_of_tasks: int
) -> Generator[User]:
    for index in range(0, len(tasks), number_of_tasks):
        address = Address(
            country=fake.country(),
            city=fake.city(),
            street=fake.street_name(),
            building_number=fake.building_number(),
            zip_code=fake.postcode(),
        )
        yield User(
            name=fake.first_name(),
            surname=fake.last_name(),
            email=fake.ascii_email(),
            address=address,
            recently_tasks=tasks[index : index + number_of_tasks],
        )


if __name__ == "__main__":
    run(main())
