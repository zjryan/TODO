import unittest
from app import create_app, db
from app.models import Task

class TaskModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_task_content(self):
        t = Task(content='cat')
        self.assertTrue(t.content is 'cat')

    def test_task_complete_default_false(self):
        t = Task()
        db.session.add(t)
        db.session.commit()
        t = Task.query.get(1)
        self.assertTrue(t.completed is False)
        db.session.delete(t)
        db.session.commit()

    def test_compelte_task_true(self):
        t = Task()
        db.session.add(t)
        db.session.commit()
        t = Task.query.get(1)
        self.assertTrue(t.completed is False)
        t.complete_task()
        self.assertTrue(t.completed is True)
        db.session.delete(t)
        db.session.commit()

    def test_generate_fake_number(self):
        Task.generate_fake(50)
        count = Task.query.count()
        self.assertTrue(count is 50)