import os
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World 2'

@app.route('/hola')
def hola_world():
    return 'Hola'

@app.route('/all/<apiname>')
def get_all_api(apiname):
    endpoints = []
    for rule in app.url_map.iter_rules():
        endpoints.append(rule.endpoint)

    print(endpoints)
    if apiname in endpoints:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)

