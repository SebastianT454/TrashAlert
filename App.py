import Ejecutar

try:
    from flask import Flask, request, jsonify, render_template

    from controller import usuario, rolesUsuario, reporte, prioridadesReporte, estadosReporte

    app = Flask(__name__)
    app.register_blueprint(usuario, url_prefix='/usuario')
    app.register_blueprint(rolesUsuario, url_prefix='/rolesUsuario')
    app.register_blueprint(reporte, url_prefix='/reporte')
    app.register_blueprint(prioridadesReporte, url_prefix='/prioridadesReporte')
    app.register_blueprint(estadosReporte, url_prefix='/estadosReporte')

    if __name__ == "__main__":
        print(" INICIANDO TRASH PROJECT BACKEND")
        app.run(debug=True)
except Exception as e:
    print("EJECUtTANDO EL ARCHIVO Ejecutar.py \n EXECUTING THE FILE Ejecutar.PY")
    Ejecutar.inicioEjecucion()