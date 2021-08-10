"""Application Entry Point"""
from app import create_app, db
from app.models import Todo

app = create_app("config.Config")

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Todo': Todo}

if __name__ == '__main__':
    app.run(debug=True)