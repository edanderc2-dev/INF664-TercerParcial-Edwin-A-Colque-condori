FROM python
COPY requirements.txt /home/myapp/
RUN pip install --no-cache-dir --progress-bar off -r /home/myapp/requirements.txt
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY sample_app.py /home/myapp/
EXPOSE 8080
CMD ["python3", "/home/myapp/sample_app.py"]
