FROM python:3.8-slim
WORKDIR /srv/tests
COPY tests/requirements.test.txt /srv/tests
RUN pip install -r requirements.test.txt
COPY tests /srv/tests