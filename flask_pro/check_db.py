from flaskpro import create_app, db
from sqlalchemy import inspect

app = create_app()

with app.app_context():
    print("sqlite:///flask_db.db", db.engine.url)
    print("['user', 'post']", inspect(db.engine).get_table_names())