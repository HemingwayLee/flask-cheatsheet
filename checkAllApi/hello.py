import os
import requests
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

@app.route('/call/<apiname>')
def call_all_api(apiname):
    rules = []
    for rule in app.url_map.iter_rules():
        rules.append(str(rule))

    print(rules)
    if "/" + apiname in rules:
        resp = requests.get(url=f"http://0.0.0.0:5000/{apiname}")
        return (resp.text, resp.status_code, resp.headers.items())
    else:
        return 'No'

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)

