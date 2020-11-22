from flask import Flask
from flask import request
from experiment import WebWindow

app = Flask(__name__)

@app.route('/')
def hello_world():
    text = input("Type whatever: ")
    return text