import unittest
from main import *

class TestEngineer(TestCase):
    def test_returns_phrase(self):
        @engineer
        def decorated(x):
            return x
        self.assertEqual(decorated("...Person"), "I'm an engineer, as well as a ...Person")
        