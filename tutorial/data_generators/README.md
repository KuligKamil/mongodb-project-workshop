# Data genertors
To fill our database with data we need to generate dummy data. For that purpose i suggest to use [Faker](https://github.com/xfxf/faker-python/blob/master/README.rst). Faker is a Python package that generates fake data for you.
List of Standard Providers you can find [here](https://faker.readthedocs.io/en/master/providers.html).


```python
from faker.factory import Factory

Faker = Factory.create
fake = Faker(locale="pl_PL")
fake.seed(2137)
```