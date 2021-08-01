import math
from functools import wraps
import unittest
from unittest import TestCase

def decorator_factory(multiplier):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * multiplier
        return wrapper
    return decorator

@decorator_factory(3)
def get_string(str):
    return str

# print(get_string("n"))


def engineer(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"I'm an engineer, as well as a {result}"
    return wrapper_func

@engineer
def introduce():
    return "...Person"

# print(introduce())
