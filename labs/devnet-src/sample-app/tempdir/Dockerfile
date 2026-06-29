FROM python
<<<<<<< HEAD
COPY requirements.txt /home/myapp/
RUN pip install --no-cache-dir --progress-bar off -r /home/myapp/requirements.txt
=======
RUN pip install flask
>>>>>>> 63b5d93e1f39a6beb11aa0ac0c78e69ab7717c6d
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY sample_app.py /home/myapp/
EXPOSE 8080
<<<<<<< HEAD
CMD ["python3", "/home/myapp/sample_app.py"]
=======
CMD python3 /home/myapp/sample_app.py
>>>>>>> 63b5d93e1f39a6beb11aa0ac0c78e69ab7717c6d
