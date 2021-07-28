import math
from functools import wraps
import unittest
from unittest import TestCase

def engineer(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"I'm an engineer, as well as a {result}"
    return wrapper_func

@engineer
def introduce():
    return "...Person"

print(introduce())
