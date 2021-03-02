import time
from flask import Flask
app = Flask(__name__)

@app.route('/long/')
def long_task():
    print("This is long running task, please wait for 10 seconds...")

    time.sleep(25) 
    return 'long running task complete'

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)

