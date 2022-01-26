from typing import Optional

from hypothesis import given
from hypothesis import given, strategies as st
from hypothesis.strategies import from_type

from fastapi.testclient import TestClient

from scripts.tutorials.arjan.pydantic_vs_dataclasses.person import Person


@given(from_type(Person))
def test_me(person: Person):
    assert isinstance(person, Person)