# Add to this file for the sample app lab
<<<<<<< HEAD
from flask import Flask, request, render_template
=======
from flask import Flask
from flask import request
from flask import render_template
>>>>>>> 63b5d93e1f39a6beb11aa0ac0c78e69ab7717c6d

sample = Flask(__name__)

@sample.route("/")
def main():
<<<<<<< HEAD
    return render_template("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False, threaded=False, processes=1)
=======
 return render_template("index.html")

if __name__ == "__main__":
 sample.run(host="0.0.0.0", port=8080)

echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile



>>>>>>> 63b5d93e1f39a6beb11aa0ac0c78e69ab7717c6d
