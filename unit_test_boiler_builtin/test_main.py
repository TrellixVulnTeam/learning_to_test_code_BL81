import unittest
from main import *
from gshclass import *
import pytest

def test_hello():
    assert "Hello testing world!" == hello()

"""class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
"""
# testing constructor of GoogleSheetHelper class
cred_path = "/home/batman/Desktop/learning_to_test_code/unit_test_boiler_builtin/master_key.json"
def test_make_helper():
    gsh1 = GoogleSheetHelper(cred_path, "google_postgres", "existing")
    assert gsh1.cred_json == cred_path
