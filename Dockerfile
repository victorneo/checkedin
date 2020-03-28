FROM python:3.6-alpine

ENV PIP_NO_CACHE_DIR false

COPY . /app
WORKDIR /app

RUN apk add --no-cache curl python3 pkgconfig python3-dev openssl-dev libffi-dev musl-dev make gcc
RUN pip install -r requirements.txt


cmd ["gunicorn", "-b 0.0.0.0", "-w 4", "checkedin.wsgi:application"]

