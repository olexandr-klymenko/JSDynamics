FROM python:3.8-slim
ADD cars_api /srv/cars_api
COPY ./requirements.txt /srv/
WORKDIR /srv
RUN pip install -r requirements.txt
