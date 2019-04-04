import time

from flask import Flask

app = Flask(__name__)

TIMEOUT = 5


@app.route('/')  # Endpoint definition --> Classic health check
def health():
    return 'Ping Python!'


@app.route('/timeout')  # Force sleep --> Simulate HTTP connection to other service or DB access
def timeout():
    time.sleep(TIMEOUT)
    return 'Timeout Python.'


@app.route('/loop')  # Heavy processing simulation
def loop():
    start = time.time()
    array = []
    message = 'Full process.'
    for i in range(1000):
        if time.time() - start > TIMEOUT:
            message = 'Time Out!'
            break
        for j in range(i):
            array.append(j)
        for x in array:
            print(f'Value: {x}')
    return f'Heavy processing Python - {message}'


if __name__ == '__main__':
    app.run()
