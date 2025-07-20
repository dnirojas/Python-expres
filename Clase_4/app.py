#-*- coding: utf-8 -*-
#
from flask import Flask, jsonify, request


app = Flask(__name__)
@app.route('/', methods=['GET'])

def unida():
    return "hola desde la Unida"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0') 