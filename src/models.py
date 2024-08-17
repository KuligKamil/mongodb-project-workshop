from enum import Enum, IntEnum
from typing import Optional

from beanie import Document
from pydantic import BaseModel


class PriorityType(IntEnum):
    low = 1
    middle = 2
    urgent = 3


# class Priority(BaseModel):
#     name: PriorityType


class SizeType(IntEnum):
    S = 1
    M = 2
    L = 3


# class Size(BaseModel):
#     value: SizeType


class Task(Document):
    name: str
    description: Optional[str] = None
    priority: Optional[PriorityType] = None
    size: Optional[SizeType] = None


class Address(BaseModel):
    country: str
    city: str
    street: str
    building_number: int
    post_code: str


class User(Document):
    name: str
    surname: str
    email: str
    address: Optional[Address] = None
    recently_tasks: Optional[list[Task]] = []


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
