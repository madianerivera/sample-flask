from flask import Flask
import os
import socket

app = Flask(__name__)


@app.route('/')
def hello():
    return f"Hello World"