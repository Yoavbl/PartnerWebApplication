#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World Hassan'}), mimetype='application/json', status=200)

@app.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World Hassan'}), mimetype='application/json', status=200)

if __name__ == '__main__':
    flaskrun(app)
