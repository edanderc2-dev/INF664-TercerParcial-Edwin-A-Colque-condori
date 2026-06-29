from flask import Flask

sample = Flask(__name__)

@sample.route("/")
<<<<<<< HEAD
def main():

    return """
    <h1>Bienvenido al Tercer Parcial de Programación de Redes</h1>
    <p>Nombre: Edwin Alexander Colque Condori</p>
    """

if __name__ == "__main__":
   
    sample.run(host="0.0.0.0", port=5055, debug=False, use_reloader=False, threaded=False, processes=1)
=======
def home():
    return "Bienvenido al Tercer Parcial de Programación de Redes\nEdwin Alexander Colque Condori"

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5055)


>>>>>>> 63b5d93e1f39a6beb11aa0ac0c78e69ab7717c6d
