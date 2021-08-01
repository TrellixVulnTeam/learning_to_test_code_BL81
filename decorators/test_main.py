import unittest
from main import *

class TestDecoratorFactory(TestCase):
    def test_string_multiplier(self):
        @decorator_factory(3)
        def string_times(n):
            return n
        self.assertEqual(string_times("n"), "nnn")

class TestEngineer(TestCase):
    def test_returns_phrase(self):
        @engineer
        def decorated(x):
            return x
        self.assertEqual(decorated("...Person"), "I'm an engineer, as well as a ...Person")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)