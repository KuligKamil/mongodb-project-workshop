# Tests with beanie and pytest.

To start working of tests in our project we need to create file `conftest.py` where we will create fixture which initialize test database. 

***Ex. 1*** - *Create a fixture that will initialize the test database. In case of an error, it will display an error and delete the database once the tests are complete.*

***HINT:*** *to drop database AsyncIOMotorClient object has property `drop_database()`*

```python
import os

import pytest_asyncio
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.models import Task, User


@pytest_asyncio.fixture(scope="session", autouse=True)
async def mongo_database_fixture():
    pass

```

To check if fixture works properly, create file `test_collection.py` with the following test function and run tests.

```python
import pytest

from src.models import User, Task


@pytest.mark.asyncio
async def test_inspect_status():
    for model in [User, Task]:
        inspected_collection = await model.inspect_collection()
        assert inspected_collection.status.value == "OK"

```

*`inspect_collection()`* - Check, if documents, stored in the MongoDB collection are compatible with the Document schema.

<details><summary><b><i>Solution to Ex. 1</i></b></summary>

```python
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

```

</details>