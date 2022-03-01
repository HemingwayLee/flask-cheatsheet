import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('template.html', my_string="Jinja2", my_list=[0,1,2,3,4,5])

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)

