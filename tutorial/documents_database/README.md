## MongoDB as a Documents Database

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


## pydantic + beanie = ❤️

To create Document in Collections we need to use the basic class in Beanie 
The basic class in Beanie is Document class to create collections of Document

After inspect of the Beanie base class Document, it's inherent from pydantic Base Model.

```python
import inspect
from beanie import Document
from pydantic import BaseModel

class User(Document):
    pass

assert issubclass(User, BaseModel)

inspect.getmro(Document)
```

Output
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

we want to create it for users

that why our first class will be user

Example in User class in pydantic

```python 
from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    email: str
```

Example in User class in beanie

```python
from beanie import Document


class User(Document):
    name: str
    surname: str
    email: str
```


if you run code above, you will see error message `CollectionWasNotInitialized`.
To Initialized collection need to use init_beanie function.


