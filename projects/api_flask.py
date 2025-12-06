# Mini API con Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/saludo/<nombre>")
def saludo(nombre):
    return jsonify({"mensaje": f"Hola {nombre}, bienvenido a la API en Flask."})

if __name__ == "__main__":
    app.run(debug=True)
