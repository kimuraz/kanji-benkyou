FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /opt/kanji-api

RUN mkdir /opt/static

RUN apt update

RUN apt-get install -y -q libpangocairo-1.0-0

COPY . .

RUN pip install -r requirements.txt
