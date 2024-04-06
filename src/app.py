from flask import Flask, render_template, request, redirect, url_for 
from config import *
from Persona import Persona

con_bd = Conexion()
app= Flask(__name__) 

@app.route('/') 
def index():  
    return render_template('index.html')

@app.route('/guardar_personas', methods=['POST']) 
def agregarPersona():
        coleccion = con_bd['Personas']
        nombre = request.form['nombre']
        correo = request.form['correo']
        comentario = request.form['comentario']

        if nombre and correo and comentario: 
            objpersona = Persona(nombre, correo, comentario)
            coleccion.insert_one(objpersona.formato_doc())
            return redirect(url_for('index'))
        else:
          return "Error"

if __name__ == '__main__':
    app.run(debug=True)