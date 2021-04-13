from flask import Flask, make_response, request
app = Flask(__name__)


@app.route('/')
def index():
    response = make_response('<h1>Welcome to my website!</h1>')
    return response
