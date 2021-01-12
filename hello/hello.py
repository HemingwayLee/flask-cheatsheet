import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route('/env')
def hello_abc():
  return f"Hello, {os.environ.get('FOOBAR', 'No env')}"

