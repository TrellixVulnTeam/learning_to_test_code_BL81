#!/usr/bin/env python
import unittest
from scripts.flask.todoApp.app import create_app, db
from scripts.flask.todoApp.app.models import Todo
from scripts.flask.todoApp.config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("config.Config")
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()
        self.populate_db()
        self.client = self.app.test_client()

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None
    
    # this must go first to populate database before you go to a route to test it as seen in "test_index"
    def populate_db(self):
        todo = Todo(todo_text='Get some really green lettuce.', complete=False)
        db.session.add(todo)
        db.session.commit()
    
    def test_database(self):
        tester = self.app.test_client(self)
        response = tester.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        assert Todo.query.first().todo_text == "Get some really green lettuce."
        assert Todo.query.first().complete == False

    def test_index_html(self):
        tester = self.app.test_client(self)
        response = tester.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)

        assert "<title>Flask Todo App</title>" in html
        assert """<link rel="stylesheet" href="/static/style.css">"""
        assert """<meta name="viewport" content="width=device-width, initial-scale=1.0">""" in html
        assert """<meta http-equiv="X-UA-Compatible" content="ie=edge">""" in html
        assert """<a href="/save_to_disk" class="btn btn-info">Download Recipe CSV</a>""" in html

if __name__ == '__main__':
    unittest.main(verbosity=2)