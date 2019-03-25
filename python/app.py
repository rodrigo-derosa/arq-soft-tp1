import time

from flask import Flask

app = Flask(__name__)

TIMEOUT = 5


@app.route('/')  # Endpoint definition
def root():
    return "Ping Python!"


@app.route('/timeout')  # Force sleep
def timeout():
    time.sleep(TIMEOUT)
    return "Timeout Python!"


if __name__ == '__main__':
    app.run()
