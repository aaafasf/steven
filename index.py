from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "El"

@app.route('/sumar')
def sumar():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        return f"Resultado de {a} + {b} = {a + b}"
    except ValueError:
        return "Parámetros inválidos. Usa /sumar?a=2&b=3"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render asigna este puerto
    print(f"Servidor iniciando en puerto {port}...")
    app.run(host="0.0.0.0", port=port)
