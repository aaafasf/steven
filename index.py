from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor corriendo correctamente en Render. Resultado: " + str(2 + 3)
    return "Servidor Flask funcionando correctamente en Render 😎"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    app.run(host="0.0.0.0", port=10000)
