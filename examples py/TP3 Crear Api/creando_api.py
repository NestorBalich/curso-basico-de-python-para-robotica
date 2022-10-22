# -*- coding: UTF-8 -*-
from flask import Flask, request  #py -m pip install Flask
import json

app = Flask(__name__)

@app.route('/api/', methods=['GET', 'POST'])
def get_users():
    response = {'message': 'hola como estas'}
    return json.dumps(response)

@app.route('/api/<string:name>/', methods=['GET', 'POST'])
def hello(name):
    response = {'message': 'hola como estas ' + name}
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)