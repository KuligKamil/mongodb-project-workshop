## data structure 
we recommend to try interactive tutorial prepared at official website mongodb.com
<!-- https://www.mongodb.com/docs/manual/tutorial/getting-started/ -->

## MongoDB as a Document Database

In MongoDB, databases hold one or more collections of documents.

Collections are analogous to tables in relational databases.

![Alt text](assets/collections.png)
Picture from mongodb.com

MongoDB stores data records as documents (specifically BSON documents) which are gathered together in collections.

![JSON vs BSON](assets/jsonvsbson.png)
JSON 
https://www.mongodb.com/resources/basics/json-and-bson

BSON specification
https://bsonspec.org/

Today, JSON shows up in many different cases:
 
* APIs
* Configuration files
* Log messages
* Database storage

However, there are several issues that make JSON less than ideal for usage inside of a database.

JSON only supports a limited number of basic data types. Most notably, JSON lacks support for datetime and binary data.

JSON objects and properties don't have fixed length which makes traversal slower.

JSON does not provide metadata and type information, taking longer to retrieve documents.

To make MongoDB JSON-first but still high-performance and general purpose, BSON was invented to bridge the gap: a binary representation to store data as JSON documents, optimized for speed, space, and efficiency. It's not dissimilar from other binary interchange formats like Protocol Buffers, or Thrift, in terms of approach.

* security not readable for people - we have tool for read it
* faster
* smaller
* contain more information

* ids in mongodb 

# add option from settings
# in beanie
# https://beanie-odm.dev/tutorial/defining-a-document/
# Settings
# The inner class Settings is used to configure:
# MongoDB collection name
# Indexes
# Encoders
# Use of revision_id
# Use of cache
# Use of state management
# Validation on save
# Configure if nulls should be saved to the database
# Configure nesting depth for linked documents on the fetch operation


# tips about configuration


<!-- https://www.mongodb.com/docs/manual/introduction/ -->

## pydantic + beanie = ❤️

the basic class in Beanie is Document class to create collections of Document

After inspect of the Beanie base class Document
we can see it's inherent from pydantic Base Model 

```python
import inspect
from beanie import Document
from pydantic import BaseModel


inspect.getmro(Document)
```

```
(beanie.odm.documents.Document,
 lazy_model.parser.new.LazyModel,
 pydantic.main.BaseModel,
 beanie.odm.interfaces.setters.SettersInterface,
 beanie.odm.interfaces.inheritance.InheritanceInterface,
 beanie.odm.interfaces.find.FindInterface,
 beanie.odm.interfaces.aggregate.AggregateInterface,
 beanie.odm.interfaces.getters.OtherGettersInterface,
 object)
```

pydantic + beanie = ❤️

### How use Document

when we would like to create application 

we want to create for users

that why our first class will be user


```python 
from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    email: str


class User(Document):
    name: str
    surname: str
    email: str
```


if you run code above, you will see error message 'CollectionWasNotInitialized'

```python 
class User(Document):
    name: str
    surname: str
    email: str


import os

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
await init_beanie(
    database=client.workshop,
    document_models=[User],
    multiprocessing_mode=True,
)
client.drop_database(name_or_database=client.workshop)
```

Okey but we don't have user.

We use will use inheritience Document class same as BaseModel class.

```python
hot_adam = User(name="Adam", surname="Brzyzek", email="hotadam@gmail.com")
hot_adam

# User(id=None, revision_id=None, name='Adam', surname='Brzyzek', email='hotadam@gmail.com')
```

```python

```
```python
hot_adam.model_dump()

{'id': None,
 'name': 'Adam',
 'surname': 'Brzyzek',
 'email': 'hotadam@gmail.com'}
```


if we check we didn't insert OUR Adam to database.
TO do it we need to use one of 5 options

insert data
* insert
* create 
* insert_one
* insert_many
* save


<!-- Remember to use await -->


### Exercise 1

* create document Task with name, description, priority(low, normal, urgent), Size(S, M, L), Status(Backlog, TODO, InProgress, OnHold, Review, Done)
* add to User Document recently task added by user  
* add one user & task


### Exercise 2

* add extend tables with technical tables like active, create_data & update_data
* create document TaskLogStatus for log task status, 
  needs to have priority, size, status, date, link to user and task

  
