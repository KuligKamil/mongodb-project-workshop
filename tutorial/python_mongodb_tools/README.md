## Comparison solution for using python with mongodb like 

We want to use mongodb for fast prototype, fast deliver, high Developer Experience and use fastapi asynchronously.

FastAPI is awesoooome <3

We found 4 potential candidates to use them. 

* pymongo [https://github.com/mongodb/mongo-python-driver](https://github.com/mongodb/mongo-python-driver)
* motor [https://github.com/mongodb/motor](https://github.com/mongodb/motor)
* mongoengine [https://github.com/MongoEngine/mongoengine](https://github.com/MongoEngine/mongoengine)
* beanie [https://github.com/BeanieODM/beanie](https://github.com/BeanieODM/beanie)


* star history comparison with [https://star-history.com/blog/how-to-use-github-star-history](https://star-history.com/blog/how-to-use-github-star-history)

[![Star History Chart](https://api.star-history.com/svg?repos=BeanieODM/beanie,mongodb/mongo-python-driver,mongodb/motor,MongoEngine/mongoengine&type=Date)](https://star-history.com/#BeanieODM/beanie&mongodb/mongo-python-driver&mongodb/motor&MongoEngine/mongoengine&Date)


no asynchronous support from PyMongo or MongoEngine

[https://mongoengine-odm.readthedocs.io/faq.html?highlight=async](https://mongoengine-odm.readthedocs.io/faq.html?highlight=async)


![star history](assets/star-history.png)

Beanie ODM - object-document mapper for MongoDB. Data models are based on Pydantic. 

Pydantic for the win.

Beanie wraps Motor, Motor wraps PyMongo. The most popular python drivers.


[https://github.com/search?q=repo%3ABeanieODM%2Fbeanie%20motor&type=code](https://github.com/search?q=repo%3ABeanieODM%2Fbeanie%20motor&type=code)
[https://github.com/search?q=repo%3Amongodb%2Fmotor%20pymongo&type=code](https://github.com/search?q=repo%3Amongodb%2Fmotor%20pymongo&type=code)

![beanie dependency](assets/beanie-dependency.png)




