from flask import Blueprint, Flask, jsonify, request


logout=  Blueprint('logout', __name__)

@logout.route('/logout', methods=['POST'])
def llamarServicioSet():
    user= request.json.get('user')
    password= request.json.get('password')
    print("User enviado: ", user, "Pass enviado:", password)