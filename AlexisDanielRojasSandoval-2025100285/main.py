#-*- Coding: utf-8 -*- 
#Caracateres especiales


from flask import Flask, jsonify, request
from cliente import cliente
app = Flask(__name__)

##Se expone el blueprint de login
app.register_blueprint(cliente)
@app.route('/', methods=['GET'])

def unida():
    return 'Si funciona'

if __name__ == '__main__':
    app.run(debug=True, port=5003, host='localhost')
