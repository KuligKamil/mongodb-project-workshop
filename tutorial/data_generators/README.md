# Data genertors
To fill our database with data we need to generate dummy data. For that purpose i suggest to use [Faker](https://github.com/xfxf/faker-python/blob/master/README.rst). Faker is a Python package that generates fake data for you.
List of Standard Providers you can find [here](https://faker.readthedocs.io/en/master/providers.html).

1. **Creation and initialization** of a Faker - dummy data generator. Below you can see the code for the init faker. I added the locale argument to return localized data from Poland. I also set the seed value to 2137, it will be helpful to compare the results of our queries later in the workshop.

```python
from faker.factory import Factory

fake = Factory.create(locale="pl_PL")
fake.seed(2137)
```

***Ex. 1*** - *Create a generator that will return the number of User objects determined in advance.*

```python
from collections.abc import Generator

from faker.factory import Factory
from faker.generator import Generator as FakerGenerator

from models import Address, PriorityType, SizeType, StatusType, Task, User


def user_generator(fake: FakerGenerator, number_of_iterations: int) -> Generator[User]:
    pass
```

<details><summary><b><i>Solution to Ex. 1</i></b></summary>

```python
from collections.abc import Generator

from faker.factory import Factory
from faker.generator import Generator as FakerGenerator

from models import Address, PriorityType, SizeType, StatusType, Task, User


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
            address=address
        )
```

</details>

***Ex. 2*** - *Using created generator in ex. 1 create async main function that will generate 50 users and save them to your database.*

```python
from asyncio import run

from database_connection import database_init


async def main():
    pass


run(main())
```

<details><summary><b><i>Solution to Ex. 2</i></b></summary>

```python
from asyncio import run

from database_connection import database_init


async def main():
    await database_init()
    fake = Factory.create(locale="pl_PL")
    fake.seed(2137)
    number_of_iterations = 50

    users = list(user_generator(fake=fake, number_of_iterations=number_of_iterations))
    await User.insert_many(users)


run(main())
```

</details>


***Ex. 3*** - *Create a generator that will return the number of Tasks for each User.*

```python
def task_generator(
    fake: FakerGenerator, users: list[User], number_of_tasks_for_user: int
) -> Generator[Task]:
    pass
```


<details><summary><b><i>Solution to Ex. 3</i></b></summary>

```python
from datetime import date


def task_generator(
    fake: FakerGenerator, users: list[User], number_of_tasks_for_user: int
) -> Generator[Task]:
    for user in users:
        for _ in range(number_of_tasks_for_user):
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
```

</details>

***Ex. 4*** - *Update the main function for generation 10 tasks for each created User and save them to your database.*

```python
from beanie.operators import In


async def main():
    pass


run(main())
```


<details><summary><b><i>Solution to Ex. 4</i></b></summary>

```python
from beanie.operators import In

async def main():
    await database_init()
    fake = Factory.create(locale="pl_PL")
    fake.seed(2137)
    number_of_iterations = 50

    users = list(user_generator(fake=fake, number_of_iterations=number_of_iterations))
    users = await User.insert_many(users)
    users = await User.find_many(
        In(User.id, users.inserted_ids),
    ).to_list()

    tasks = list(task_generator(fake=fake, users=users, number_of_tasks_for_user=10))
    await Task.insert_many(tasks)


run(main())
```

</details>


***Ex. 5*** - *Create a function that updates all users and saves their last recent tasks. Also update main function to execute that function and saves last 3 tasks for each user.*

```python
from pymongo import DESCENDING


async def user_update_recent_tasks(users: list[User], number_of_tasks: int):
    pass


async def main():
    pass


run(main())
```

<details><summary><b><i>Solution to Ex. 5</i></b></summary>

```python
from pymongo import DESCENDING


async def user_update_recent_tasks(users: list[User], number_of_tasks: int):
    for user in users:
        tasks = (
            await Task.find_many(Task.user.id == PydanticObjectId(user.id))
            .sort((Task.create_date, DESCENDING))
            .to_list(number_of_tasks)
        )
        user.recently_tasks = tasks
        await user.save()


async def main():
    await database_init()
    fake = Factory.create(locale="pl_PL")
    fake.seed(2137)
    number_of_iterations = 50

    users = list(user_generator(fake=fake, number_of_iterations=number_of_iterations))
    users = await User.insert_many(users)
    users = await User.find_many(
        In(User.id, users.inserted_ids),
    ).to_list()

    tasks = list(task_generator(fake=fake, users=users, number_of_tasks_for_user=10))
    tasks = await Task.insert_many(tasks)
    tasks = await Task.find_many(
        In(Task.id, tasks.inserted_ids),
    ).to_list()
    await user_update_recent_tasks(users=users, number_of_tasks=3)
```

</details>