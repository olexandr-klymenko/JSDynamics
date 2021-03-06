FROM python:3.8-slim as base
ADD cars_api /srv/cars_api
COPY ./requirements.txt /srv/
COPY tests /srv/tests
WORKDIR /srv
RUN pip install -r requirements.txt
