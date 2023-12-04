import os
import json
import base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World 2'

@app.route('/inpaint', methods=['POST'])
def inpaint():
    content = request.json
    print(content['img'])
    print(content['mask'])

    return 'yes'

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)

