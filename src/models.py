from datetime import datetime
from enum import Enum, IntEnum
from typing import ClassVar, ForwardRef, Optional

from beanie import Document, Link
from pydantic import BaseModel


class Date(BaseModel):
    create_date: datetime = datetime.now()
    update_date: datetime = datetime.now()


class Active(BaseModel):
    active: bool = True


class PriorityType(IntEnum):
    low = 1
    middle = 2
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


User = ForwardRef("User")


# https://beanie-odm.dev/tutorial/multi-model-pattern/
# class TaskBase(Date):
#     priority: Optional[PriorityType] = None
#     size: Optional[SizeType] = None
#     status: StatusType = StatusType.BACKLOG


class Task(Document, Date, Active):
    name: str
    description: Optional[str] = None
    priority: Optional[PriorityType] = None
    size: Optional[SizeType] = None
    status: StatusType = StatusType.BACKLOG
    user: Link[User]


class Address(BaseModel):
    country: str
    city: str
    street: str
    building_number: str
    zip_code: str


class User(Document, Date, Active):
    name: str
    surname: str
    email: str
    address: Optional[Address] = None
    recently_tasks: Optional[list[Task]] = []


class TaskLogStatus(Document, Date):
    priority: Optional[PriorityType] = None
    size: Optional[SizeType] = None
    status: StatusType = StatusType.BACKLOG
    date: datetime = datetime.now()
    task: Link[Task]
    user: Link[User]
    # last_status: StatusType = StatusType.BACKLOG
    # new_status: StatusType = StatusType.BACKLOG
    # start_date: datetime = datetime.now()
    # end_date: datetime = datetime.now()
