from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",   
    password="ramm160799",
    database="prueba1"
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        sexo = request.form['sexo']
        edad = request.form['edad']

        cursor = db.cursor()
        sql = "INSERT INTO alumnos (nombre, sexo, edad) VALUES (%s, %s, %s)"
        val = (nombre, sexo, edad)

        cursor.execute(sql, val)
        db.commit()

    cursor = db.cursor()
    cursor.execute("SELECT nombre, sexo, edad FROM alumnos")
    alumnos = cursor.fetchall()

    return render_template('Diseno.html', alumnos=alumnos)

if __name__ == "__main__":
    app.run(debug=True)
