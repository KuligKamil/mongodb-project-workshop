## Comparison solution for using Python with MongoDB 

We want to use mongodb for fast prototype, fast deliver, high Developer Experience and use FastAPI asynchronously.

FastAPI is awesoooome <3

We found 4 potential candidates to use them. 

* pymongo [https://github.com/mongodb/mongo-python-driver](https://github.com/mongodb/mongo-python-driver)
  
* motor [https://github.com/mongodb/motor](https://github.com/mongodb/motor)
  
* mongoengine [https://github.com/MongoEngine/mongoengine](https://github.com/MongoEngine/mongoengine)
  
* beanie [https://github.com/BeanieODM/beanie](https://github.com/BeanieODM/beanie)


### star history comparison with [https://star-history.com/blog/how-to-use-github-star-history](https://star-history.com/blog/how-to-use-github-star-history)

[![Star History Chart](https://api.star-history.com/svg?repos=BeanieODM/beanie,mongodb/mongo-python-driver,mongodb/motor,MongoEngine/mongoengine&type=Date)](https://star-history.com/#BeanieODM/beanie&mongodb/mongo-python-driver&mongodb/motor&MongoEngine/mongoengine&Date)


![star history](assets/star-history.png)

[https://mongoengine-odm.readthedocs.io/faq.html?highlight=async](https://mongoengine-odm.readthedocs.io/faq.html?highlight=async)


PyMongo and Motor are Python drivers.

MongoEngine and Beanie are ODMs.

Document-Object Mapper (think ORM, but for document databases).

PyMongo and MongoEngine out - no asynchronous support from PyMongo or MongoEngine.

For enter easier in MongoDB world & hype about tool we decide to use Beanie.

Beanie ODM - object-document mapper for MongoDB. Data models are based on Pydantic. 

<!-- how many of use like Pydantic -->

Pydantic for the win.

Beanie wraps Motor, Motor wraps PyMongo. The most popular python drivers.

[https://github.com/search?q=repo%3ABeanieODM%2Fbeanie%20motor&type=code](https://github.com/search?q=repo%3ABeanieODM%2Fbeanie%20motor&type=code)
[https://github.com/search?q=repo%3Amongodb%2Fmotor%20pymongo&type=code](https://github.com/search?q=repo%3Amongodb%2Fmotor%20pymongo&type=code)

![beanie dependency](assets/beanie-dependency.png)


## [OPTIONAL INFO] Mongoose [https://www.mongodb.com/docs/mongodb-shell/](https://www.mongodb.com/docs/mongodb-shell/)

The MongoDB Shell, mongosh, is a JavaScript and Node.js REPL environment for interacting with MongoDB deployments in Atlas  , locally, or on another remote host. Use the MongoDB Shell to test queries and interact with the data in your MongoDB database.

If you would like more native approach in MongoDB