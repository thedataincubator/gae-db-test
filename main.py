import time
import json
import os

from flask import Flask, render_template, request
from google.appengine.ext import ndb

app = Flask(__name__)

if os.getenv('FLASK_DEBUG'):
  app.debug = True

@app.route('/')
def index():
  return "hello"

class A(ndb.Model):
  t = ndb.TextProperty('t')
  r = ndb.KeyProperty('r', kind='B')


class B(ndb.Model):
  t = ndb.TextProperty('t')

@ndb.tasklet
def _add():
  b_key = yield B(t="b").put_async()
  yield A(t="a", r=b_key).put_async()

@app.route('/add')
@ndb.synctasklet
def add():
  n = int(request.args.get("n", 10))
  adds = [_add] * n
  async = int(request.args.get("async", 0))

  start = time.time()
  if async:
    yield [a() for a in [_add] * n]
  else:
    for a in adds:
      yield a()
  end = time.time()

  raise ndb.Return(
    json.dumps({
      "objects": n,
      "time": end - start,
      "async": async
    })
  )

@app.route('/counts')
@ndb.synctasklet
def counts():
  counts = yield A.query().count_async(), B.query().count_async()
  raise ndb.Return("A: {}, B: {}".format(*counts))
