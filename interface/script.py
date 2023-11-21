from flask import Flask
from flask import render_template
import pickle


app = Flask(__name__)

@app.route("/")
def hello_world(name=None):
    return render_template('hello.html', name=name)