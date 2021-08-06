from scripts.flask import flask_main
import unittest


class HomeTestCase(unittest.TestCase):

  def test_index(self):
    tester = flask_main.app.test_client(self)
    response = tester.get('/', content_type='application/json')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, b"Hello World!")

if __name__ == '__main__':
    unittest.main()