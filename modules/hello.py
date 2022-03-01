import os
from flask import Flask
from mod import mylib
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Mod ' + mylib.say_hi()

if __name__ == '__main__':
    # debug=True will be hot reloading mode
    app.run('0.0.0.0', 5000, threaded=True, debug=True)

