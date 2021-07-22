import main
from main import app
import unittest
import json

def test_case_1():
    assert -2 == main.doubleInt(0)

def test_case_2():
    assert 2 == main.doubleInt(1)


class HomeTestCase(unittest.TestCase):

  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/', content_type='application/json')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, b"Hello World!")
if __name__ == '__main__':
    unittest.main()