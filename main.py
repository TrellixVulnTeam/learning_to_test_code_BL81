import os
from flask import Flask
from flask import Response
from flask import json

def doubleInt(n):
    if n <= 0:
        return -2
    return n * 2

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
