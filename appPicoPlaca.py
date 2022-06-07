# Nombre: Jhostyn Javier Gavilanez Suarez

# importar la libreria flask
#En este apartado se añade la libreria de flask, entre otras para hacer el llamado y otras funcionalidades de la pagina del sistema de control.
from flask import Flask, render_template, redirect, request, url_for

# ---------------------------------------------------------------------------
# Se inicializa y se llama a la carpeta  de templates y el programa en si 
app = Flask(__name__, template_folder='templates')

# ---------------------------------------------------------------------------
# Este es el arreglo para almacenar las tareas en forma de lista
ListasRegistros = []  # arreglo de la lista
# ---------------------------------------------------------------------------
# Password para tener acceso a dicha aplicacion mediante el uso del secret key
app.secret_key = 'jhostyn123'

# ---------------------------------------------------------------------------
# Este es el primer paso ver las listas de las tareas pendientes
# Esta es la ruta raiz donde esta nuestro html controlador  raiz
# este es el controlador donde me permite ingresar los registros del cliente 
@app.route('/')
# llamar a index.html en la ruta principal
def panelPrincipal():
    return render_template('/principal.html', ListasRegistros=ListasRegistros)

# ---------------------------------------------------------------------------
# Este es el segundo paso para enviar datos a nuestra el Registro mediante el formulario dado.
# Controlador de envio.

@app.route('/enviarRegistros', methods=['POST'])
# metodo de guardar los datos
def enviarRegistros():  # Aqui realiza el envio de datos para ser guardados en la lista.
    if request.method == 'POST':
        # el mensaje de añadir un registro de un nuevo dato se muestra por codigo javascript en el html
        Registro_NroLlamada = request.form['Registro_NroLlamada']
        Registro_PlacaVehicular = request.form['Registro_PlacaVehicular']
        Registro_Fecha = request.form['Registro_Fecha']
        Registro_Hora = request.form['Registro_Hora']
        Registro_Prediccion = request.form['Registro_Prediccion']

        # El mensaje esta por codigo javascript dentro del HTML
        if Registro_NroLlamada == '' or Registro_PlacaVehicular == '' or Registro_Fecha == '' or Registro_Hora == '' or Registro_Prediccion == '' :
            return redirect(url_for('panelPrincipal'))
        else:
            ListasRegistros.append(
                {'Registro_NroLlamada': Registro_NroLlamada,
                 'Registro_PlacaVehicular': Registro_PlacaVehicular,
                 'Registro_Fecha': Registro_Fecha,
                 'Registro_Hora':Registro_Hora,
                 'Registro_Prediccion':Registro_Prediccion})

            return redirect(url_for('panelPrincipal'))


# ---------------------------------------------------------------------------
# Controlador de la ruta para borrar todos los datos encontrados del registro 
# Controlador de borrar registros del cliente
@app.route('/borrarRegistros', methods=['POST'])
def borrarRegistros():              # La funcion de envio de mensaje borrado se hace mediante codigo Javascript
    ListasRegistros.clear()
    return redirect(url_for('panelPrincipal'))





# ejecutar del main principal para nuestra pagina 
if __name__ == '__main__':

    app.run(debug=True)