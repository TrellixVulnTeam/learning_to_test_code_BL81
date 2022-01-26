from typing import Optional

from hypothesis import given
from hypothesis.strategies import from_type
from pydantic import BaseModel


class Adress(BaseModel):
    city: str
    street: str
    house_number: int
    postal_code: int


class Person(BaseModel):
    prename: str
    middlename: Optional[str]
    lastname: str
    address: Adress


