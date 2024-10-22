```python
from src.database_connection import database_init
from asyncio import run
from beanie import Document


class User(Document):
    name: str
    surname: str
    email: str


run(database_init(document_models=[User]))
```

Do you see Schema in Atlas?


Okey, but we don't have Document.

We use will use inheritance Document class same as BaseModel class.

```python
hot_adam = User(name="Adam", surname="Brzyzek", email="hotadam@gmail.com")
hot_adam
```

Output
```python
User(id=None, revision_id=None, name='Adam', surname='Brzyzek', email='hotadam@gmail.com')
```

We can see two additional attributes. `id` and `revision_id`.

`id` field reflects the unique _id field of the MongoDB document. Each object of the Document type has this field. The default type of this is PydanticObjectId.

`revision_id` field is for feature helps with concurrent operations.

We can use Base Model methods.


```python
hot_adam.model_dump()

{'id': None,
 'name': 'Adam',
 'surname': 'Brzyzek',
 'email': 'hotadam@gmail.com'}
```

Value of id field mean that we didn't insert to database yet.

To insert OUR Adam to database we need to use one of 5 options

* **insert** - basic method to insert Document
* **insert_many** - to insert one or more Documents
* **save** - insert, update current object of class Document to database
* create, insert_one - synonyms for insert 

Remember for each use await key word otherwise you will return couritne object & you will not insert object.

```python
hot_adam = User(name="Adam", surname="Brzyzek", email="hotadam@gmail.com")
```

```python
await hot_adam.save()
```
 or 

```python
await User.save(hot_adam)
```
 or

```python
await hot_adam.insert()
```

 or

```python
await User.insert(hot_adam)
```

```python
hot_adam.model_dump()
```

Output
```python 
{'id': '66cb3c4631b062a669d4357c',
 'name': 'Adam',
 'surname': 'Brzyzek',
 'email': 'nothotadam@gmail.com'}
```

How to get data?
* **find** - basic function to get 
  * **to_list**
  * **first_or_none**
  
* get - get document with id, without filtering
* find_one - get one document with filtering
* find_all - synonyms to find({})

Get all users in database

```python
users = await User.find().to_list()
```

Get first user in database

```python
result = await User.find().first_or_none()
```

Filters Adams

```python
adams = await User.find(User.name == "Adam").to_list()
```

### Exercise 1 - Create Document
* create document Task with name, description, priority(low, normal, urgent), Size(S, M, L), Status(Backlog, TODO, InProgress, OnHold, Review, Done)
* add one user & task

example of priority type

```python
from enum import IntEnum


class PriorityType(IntEnum):
    low = 1
    normal = 2
    urgent = 3
```


<details><summary><b><i>Solution</i></b></summary>

```python
from enum import IntEnum
from typing import Optional
from pydantic import BaseModel
from asyncio import run
from beanie import Document


class PriorityType(IntEnum):
    low = 1
    normal = 2
    urgent = 3


class SizeType(IntEnum):
    S = 1
    M = 2
    L = 3


class StatusType(IntEnum):
    BACKLOG = 1
    TODO = 2
    InProgress = 3
    OnHold = 4
    Review = 5
    Done = 6


class Task(Document):
    name: str
    description: Optional[str] = None
    priority: Optional[PriorityType] = None
    size: Optional[SizeType] = None
    status: StatusType = StatusType.BACKLOG


class User(Document):
    name: str
    surname: str
    email: str

run(database_init(document_models=[User, Task]))
```

</details>


You can always extend your Document with other classes like with pydantic classes.

For example we can add technical attribute if user is active and reuse it in the task too.


```python
from pydantic import BaseModel
from beanie import Document

class Active(BaseModel):
  active: bool = True


class User(Document, Active):
    name: str
    surname: str
    email: str

hot_adam = User(
    name="Adam",
    surname="Brzyzek",
    email="hotadam@gmail.com")

hot_adam.model_dump()
```

Output
```python
{'active': True,
 'id': None,
 'name': 'Adam',
 'surname': 'Brzyzek',
 'email': 'hotadam@gmail.com'}
```


In a relational database, you store each individual entity in its own table, and link them together through foreign keys. While MongoDB certainly supports references from one document to another, and even multi-document joins, it’s a mistake to use a document database the same way you use a relational one.


Embedded documents are an efficient and clean way to store related data, especially data that’s regularly accessed together. 

In general, when designing schemas for MongoDB, you should prefer embedding by default, and use references and application-side or database-side joins only when they’re worthwhile. The more often a given workload can retrieve a single document and have all the data it needs, the more consistently high-performance your application will be.

Link to documentation for MongoDB - Embedding MongoDB
[https://www.mongodb.com/resources/products/fundamentals/embedded-mongodb](https://www.mongodb.com/resources/products/fundamentals/embedded-mongodb)

Example Embedded Document - User Address

```python
from pydantic import BaseModel
from beanie import Document
from typing import Optional


class Address(BaseModel):
    country: str
    city: str
    street: str
    building_number: str
    zip_code: str


class User(Document):
    name: str
    surname: str
    email: str
    address: Optional[Address] = None

hot_adam = User(
    name="Adam",
    surname="Brzyzek",
    email="hotadam@gmail.com",
    address=Address(
        country="Poland",
        city="Gliwice",
        street="Jana Matejki 3",
        building_number="IBU Craft Beers",
        zip_code="44-100",
    ),
)
```

Our Favorite bar in Gliwice [https://maps.app.goo.gl/Jscx2wCmkE5cr2ke9](https://maps.app.goo.gl/Jscx2wCmkE5cr2ke9)


### Exercise 2 - create Embedded Document & extend Document
* add to User Document recent tasks, added by user
* add extend classes with technical fields like active, create_date & update_date
* add one user & one task

<details><summary><b><i>Solution</i></b></summary>

```python
from pydantic import BaseModel
from beanie import Document
from typing import Optional
from datetime import datetime


class Date(BaseModel):
    create_date: datetime = datetime.now()
    update_date: datetime = datetime.now()


class Address(BaseModel):
    country: str
    city: str
    street: str
    building_number: str
    zip_code: str


class User(Document, Active, Date):
    name: str
    surname: str
    email: str
    address: Optional[Address] = None
    recently_tasks: Optional[Task] = None
```

</details>


## Relations
The document can contain links to other documents in their fields.

Example add link Task to User


```python
from asyncio import run
from pydantic import BaseModel
from beanie import Document
from typing import Optional


User = ForwardRef("User")

class Task(Document, Date, Active):
    name: str
    status: StatusType = StatusType.BACKLOG
    user: Link[User]

class User(Document, Date, Active):
    name: str
    surname: str
    email: str
    address: Optional[Address] = None
    recently_tasks: Optional[list[Task]] = []


run(database_init(document_models=[User, Task], clear_database=True))

hot_adam = User(name="Adam",surname="Brzyzek",email="hotbrzyzek@gmail.com")

await User.insert(hot_adam)

tasks = [
    Task(name="sail", user=hot_adam.id), # TODO: CHECK IF IT WORKING with hot_adam without id
    Task(name="drink beers", user=hot_adam.id),
]
await Task.insert_many(tasks)
user.recently_tasks = tasks
await user.save()
```


### Exercise 3 - link to other Document
* create document TaskLogStatus for log task status, 
  needs to have priority, size, status, date, link to user and task
* add task change status

<details><summary><b><i>Solution</i></b></summary>

```python
class TaskLogStatus(Document, Date):
    priority: Optional[PriorityType] = None
    size: Optional[SizeType] = None
    status: StatusType = StatusType.BACKLOG
    date: datetime = datetime.now()
    task: Link[Task]
    user: Link[User]
```

</details>


Updating & Deleting 
documentation: [https://beanie-odm.dev/tutorial/updating-%26-deleting/](https://beanie-odm.dev/tutorial/updating-%26-deleting/)

For update we have couple options
* save
* replace -  throws: - a ValueError if the document does not have an id yet, or - a beanie.exceptions.DocumentNotFound
* update, set, inc - can be performed on the result of a find or find_one query, or on a document that was returned from an earlier query.
* set
* upsert - to insert a document when no documents are matched against the search criteri

```python
user = await User.find(User.name == "Adam").first_or_none()
user = await user.set({User.name: "John"})
user.model_dump()
```
 
Output
```python
{'id': '66cbc95d9721746de2ec9ee6',
 'name': 'John',
 'surname': 'Brzyzek',
 'email': 'hotbrzyzek@gmail.com'}
```

To delete use method delete() XD

```python
toxic_workshop_instructor = await User.find_one(User.name == "Kamil")
await toxic_workshop_instructor.delete()
```

### Exercise 4 - update, delete

* Update task and user with 2 different method.
* Delete something or somebody. Do it 

<details><summary><b><i>Solution</i></b></summary>
Come on. Don't cheat XD
</details>
  

## important mentions 
* This returns a FindMany object, which can be used to access the results in different ways. To loop through the results, use a async for loop:

```python
async for result in User.find():
    print(result)
```

* When only a part of a document is required, projections can save a lot of database bandwidth and processing. 
  For simple projections we can just define a pydantic model with the required fields and pass it to project() method

```python
class UserBasicInfo(BaseModel):
    name: str
    surname: str


adams = await User.find(User.name == "Adam").project(UserBasicInfo).to_list()
adams
```

Output
```python
[]

```

* Settings
    add option from settings [https://beanie-odm.dev/tutorial/defining-a-document/](https://beanie-odm.dev/tutorial/defining-a-document/)
    

* We recommend to try interactive tutorial prepared at official website mongodb.com [https://www.mongodb.com/docs/manual/tutorial/getting-started/](https://www.mongodb.com/docs/manual/tutorial/getting-started/ )


* Good to check setting parameter is_root = True
[https://beanie-odm.dev/tutorial/inheritance/](https://beanie-odm.dev/tutorial/inheritance/)

