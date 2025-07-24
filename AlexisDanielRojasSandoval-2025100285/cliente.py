from flask import Blueprint, Flask, jsonify, request


cliente=  Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])

def llamarServicioSet():
    ci= request.json.get('ci')

    print("Numero de cedula enviado enviado: ",ci)

    codRes, menRes, accion, apellidos, nombre = inicializarVariables(ci)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'ci': ci,
        'accion': accion,
        'apellido': apellidos,
        'nombre': nombre,
    }  
    return jsonify(salida) 


def inicializarVariables(ci):
    codRes = 'SIN_ERROR'
    menRes = "OK"
    accion = "Login exitoso"
    ciLocal = "6773682"
    nombreLocal = "Alexis"
    apellidoLocal= "Rojas Sandoval"

    try:
        if ci == ciLocal :
            print("Login exitoso")
            print(nombreLocal)
            print(apellidoLocal)
            accion = "Login exitoso"
        else:
            codRes = 'ERROR'
            menRes = "Error de Cliente"
            accion = "Cliente no esta en el sistema"
            ci = '6773682'

    except Exception as e:
        print("Error en el login:", e)
        codRes = 'ERROR'
        menRes = "Error"
        accion = "Error"
        return codRes, menRes, accion,

    

