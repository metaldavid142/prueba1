#Se importa la biblioteca de Flask
from flask import Flask, redirect, render_template, request, url_for, flash

#Objeto para inicializar la aplicación
#1. Nombre por defecto
#2. Ruta donde están los templates
app = Flask(__name__, template_folder='templates')

#Almacenamiento de registros
registro_covid = []

#Primer controlador: inicial
#Lista actual de tareas pendientes y Formulario HTML para ingresar nuevas tareas
@app.route('/')
def principal():
    return render_template('principal.html', registro_covid=registro_covid)


#Controlador: registro de cuenta
@app.route('/registrar_cuenta', methods=['POST'])
def registrar_cuenta():
    if request.method == 'POST':
        
        #Campos a llenar
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        estado = request.form['estado']

        #Validación para que los campos no sean nulos
        if nombre == '' or telefono == '':
            flash('LLenar todos los campos')
            return redirect(url_for('principal'))
        
        else:
            flash('Cuenta registrada exitosamente!')
            registro_covid.append({'nombre': nombre, 'telefono': telefono, 'estado': estado})
            return redirect(url_for('principal'))
        
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        
        #Campos a llenar
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        estado = request.form['estado']

        #Validación para que los campos no sean nulos
        if nombre == '' or telefono == '':
            flash('LLenar todos los campos')
            return redirect(url_for('principal'))
        
        else:
            flash('Cuenta registrada exitosamente!')
            registro_covid.append({'nombre': nombre, 'telefono': telefono, 'estado': estado})
            return redirect(url_for('principal'))


#Controlador: Limpiar los registros
@app.route('/borrar', methods=['POST'])
def borrar():
    if request.method == 'POST':
        
        #Verificación de la lista de tareas
        if registro_covid == []:
            flash('Registros vacios')
            return redirect(url_for('principal'))

        else:
            registro_covid.clear()
            flash('Registros vacios')
            return redirect(url_for('principal'))

#Método para correr la aplicación
if __name__ == '__main__':
    app.run(debug=True)