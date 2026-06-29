<<<<<<< HEAD
#!/bin/bash
echo "Creando directorios temporales..."
mkdir -p tempdir/templates
mkdir -p tempdir/static

echo "Copiando archivos..."
cp sample_app.py tempdir/
cp -r templates/* tempdir/templates/
cp -r static/* tempdir/static/
cp requirements.txt tempdir/   # copiamos también el requirements.txt

echo "Generando Dockerfile..."
echo "FROM python" > tempdir/Dockerfile
echo "COPY requirements.txt /home/myapp/" >> tempdir/Dockerfile
echo "RUN pip install --no-cache-dir --progress-bar off -r /home/myapp/requirements.txt" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD [\"python3\", \"/home/myapp/sample_app.py\"]" >> tempdir/Dockerfile

echo "Construyendo contenedor Docker..."
cd tempdir
docker build -t sampleapp .

echo "Ejecutando contenedor..."
docker run -t -d -p 5050:5050 --name samplerunning sampleapp

echo "Contenedores activos:"
docker ps -a
=======
#!/bin.bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp sample_app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/sample_app.py" >> tempdir/Dockerfile

cd tempdir
docker build -t sampleapp .
docker run -t -d -p 8080:8080 --name samplerunning sampleapp
docker ps -a

>>>>>>> 63b5d93e1f39a6beb11aa0ac0c78e69ab7717c6d
