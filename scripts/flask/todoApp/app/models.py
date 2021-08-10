from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_text = db.Column(db.Text(), nullable=False)
    complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Task: {}>, <Status: {}'.format(self.text, self.complete)
        
# >>> from app import db
# >>> from app.models import Hero, Story
# >>> db.create_all()