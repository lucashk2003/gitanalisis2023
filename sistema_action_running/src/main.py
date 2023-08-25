from flask import Flask, request, render_template
from confiDB import * #Importando conexion BD


app = Flask(__name__) 


@app.route('/') 
def inicio(): 
    return render_template('pages/selectturno.html')

@app.route('/form', methods=['GET', 'POST'])
def registrarForm():
    msg =''
    if request.method == 'POST':
        idcliente           = request.form['idcliente']
        horainicio          = request.form['horainicio']
        horafin             = request.form['horafin']
        
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)

        sql         = ("INSERT INTO turnos(idcliente, hora_inicio, hora_fin) VALUES (%s, %s, %s)")
        valores     = (idcliente, horainicio, horafin)

        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        msg = 'Registro con exito'
        
        print(cursor.rowcount, "registro insertado")
        print("1 registro insertado, id", cursor.lastrowid)
  
        return render_template('pages/selectturno.html', msg='Formulario enviado')
    else:
        return render_template('pages/selectturno.html', msg = 'Metodo HTTP incorrecto')


if __name__ == '__main__': 
    app.run(debug=True, port=5000) 