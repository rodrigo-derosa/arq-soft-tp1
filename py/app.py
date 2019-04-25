import time
import random

from flask import Flask

app = Flask(__name__)
cache_instance = []

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
        for k in range(len(array)):
            array[k] *= array[k]
    return f'Heavy processing Python - {message}'

@app.route('/cache')
def cache():
    number = random.randint(1,20)
    result = 'Your number is {}'.format(number)
    if number not in cache_instance:
        time.sleep(1) # Simulate Service/DB access
        cache_instance.append(number) # Now we have the result cached
    return result


if __name__ == '__main__':
    app.run()
