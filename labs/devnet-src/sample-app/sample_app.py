from flask import Flask

sample = Flask(__name__)

@sample.route("/")
def home():
    return "Bienvenido al Tercer Parcial de Programación de Redes\nEdwin Alexander Colque Condori"

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5055)


