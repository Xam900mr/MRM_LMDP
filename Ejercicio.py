from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ramm160799",
    database="prueba1"
)

@app.route('/', methods=['GET'])
def index():
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()

    return render_template('Diseno.html', alumnos=alumnos, alumno_edit=None)

@app.route('/insert', methods=['POST'])
def insert():
    cursor = db.cursor()
    alumno_id = request.form['id']
    nombre = request.form['nombre']
    sexo = request.form['sexo']
    edad = request.form['edad']

    if alumno_id:
        sql = "UPDATE alumnos SET nombre = %s, sexo = %s, edad = %s WHERE id = %s"
        val = (nombre, sexo, edad, alumno_id)
        
    else:  
        sql = "INSERT INTO alumnos (nombre, sexo, edad) VALUES (%s, %s, %s)"
        val = (nombre, sexo, edad)

    cursor.execute(sql, val)
    db.commit()

    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM alumnos WHERE id = %s", (id,))
    alumno = cursor.fetchone()

    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()

    return render_template('Diseno.html', alumnos=alumnos, alumno_edit=alumno)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor = db.cursor()
    sql = "DELETE FROM alumnos WHERE id = %s"
    cursor.execute(sql, (id,))
    db.commit()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)