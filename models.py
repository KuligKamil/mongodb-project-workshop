from enum import IntEnum
from typing import Optional

from beanie import Document
from pydantic import BaseModel


class PriorityType(IntEnum):
    low = 1
    middle = 2
    urgent = 3


class SizeType(IntEnum):
    S = 1
    M = 2
    L = 3


class Task(Document):
    name: str
    description: Optional[str] = None
    priority: Optional[PriorityType] = None
    size: Optional[SizeType] = None


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
    address: Address
    recently_tasks: Optional[list[Task]] = []
