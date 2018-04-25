from flask import Flask, render_template, request
from google.appengine.ext import ndb

app = Flask(__name__)

@app.route('/')
def form():
    return "hello"
