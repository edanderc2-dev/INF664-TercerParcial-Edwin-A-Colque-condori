# Add to this file for the sample app lab
from flask import Flask, request, render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False, threaded=False, processes=1)
