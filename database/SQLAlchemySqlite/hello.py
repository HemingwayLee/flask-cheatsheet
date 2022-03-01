import os
from flask import Flask, jsonify
from mydb.database import db_session, init_db
from mydb.models import User

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, ORM'

@app.route('/create/')
def create_db():
    init_db()
    return 'created'

@app.route('/add/')
def add_user():
    u = User('admin', 'admin@localhost')
    db_session.add(u)
    db_session.commit()
    return 'added'

@app.route('/query/')
def query_db():
    print(User.query.all())
    users = User.query.all()
    ret = users[0].serialize()
    print(ret)
    return str(ret)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)

