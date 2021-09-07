MAINTAINER Serg Pomytkin

FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ADD app/main.py main.py

EXPOSE 8000

CMD gunicorn --bind 0.0.0.0:8000 --workers=4 wsgi:app

