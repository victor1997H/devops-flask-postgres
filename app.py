from flask import Flask
import psycopg2

app = Flask(__name__)

VERSION = "3.0.0"

@app.route("/")
def inicio():

    try:
        conexion = psycopg2.connect(
            host="db",
            database="empresa",
            user="admin",
            password="admin123"
        )

        cursor = conexion.cursor()

        cursor.execute("SELECT nombre FROM clientes;")
        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        lista = "".join([f"<li>{d[0]}</li>" for d in datos])

        return f"""
        <h1>Clientes desde PostgreSQL</h1>
        <h2>Versión {VERSION}</h2>
        <ul>
            {lista}
        </ul>
        """

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)