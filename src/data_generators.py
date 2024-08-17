from asyncio import run
from collections.abc import Generator
from datetime import date

from beanie import PydanticObjectId
from beanie.operators import In
from faker.factory import Factory
from faker.generator import Generator as FakerGenerator

from database_connection import database_init
from models import Address, PriorityType, SizeType, StatusType, Task, User


async def main():
    await database_init()
    Faker = Factory.create
    fake = Faker(locale="pl_PL")
    fake.seed(2137)
    number_of_iterations = 50

    users = list(user_generator(fake=fake, number_of_iterations=number_of_iterations))
    users = await User.insert_many(users)
    users = await User.find_many(
        In(User.id, users.inserted_ids),
    ).to_list()

    tasks = list(task_generator(fake=fake, users=users, nuber_of_tasks_for_user=10))
    tasks = await Task.insert_many(tasks)
    tasks = await Task.find_many(
        In(Task.id, tasks.inserted_ids),
    ).to_list()
    await user_update_recent_tasks(users=users, number_of_tasks=3)


def task_generator(
    fake: FakerGenerator, users: list[User], nuber_of_tasks_for_user: int
) -> Generator[Task]:
    for user in users:
        for _ in range(nuber_of_tasks_for_user):
            create_date = user.create_date + fake.time_delta(
                end_datetime=date(2026, 1, 1)
            )
            yield Task(
                create_date=create_date,
                update_date=create_date,
                active=fake.pybool(truth_probability=90),
                name=fake.pystr(prefix="task_", max_chars=10),
                description=fake.pystr(prefix="description_", max_chars=10),
                priority=fake.enum(PriorityType),
                size=fake.enum(SizeType),
                status=fake.enum(StatusType),
                user=user,
            )


def user_generator(fake: FakerGenerator, number_of_iterations: int) -> Generator[User]:
    for _ in range(number_of_iterations):
        address = Address(
            country=fake.country(),
            city=fake.city(),
            street=fake.street_name(),
            building_number=fake.building_number(),
            zip_code=fake.postcode(),
        )
        creation_date = fake.date_time_this_year(before_now=True, after_now=False)
        yield User(
            create_date=creation_date,
            update_date=creation_date,
            active=fake.pybool(truth_probability=90),
            name=fake.first_name(),
            surname=fake.last_name(),
            email=fake.ascii_email(),
            address=address,
        )


async def user_update_recent_tasks(users: list[User], number_of_tasks: int):
    for user in users:
        tasks = (
            await Task.find_many(Task.user.id == PydanticObjectId(user.id))
            .sort()
            .to_list(number_of_tasks)
        )
        print(user, tasks)
        user.recently_tasks = tasks
        responce = await user.save()
    print(responce)


run(main())
