from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!' 

@app.route('/abc')
def hello_abc():
  return 'Hello, ABC!' 

@app.route('/user/<username>')
def show_user(username):
  return f"Hello, {username}"

@app.route('/post/<int:id>')
def show_id(id):
  return f'Post id is {id}'

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    return "you are POST method"
  else:
    return "I am GET method"
