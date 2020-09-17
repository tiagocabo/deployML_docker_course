FROM python:3

MAINTAINER Tiago Cabo
COPY . /usr/local/python/rf_api/
EXPOSE 5000
WORKDIR /usr/local/python/rf_api/

RUN pip install --upgrade pip && pip install -r requirements.txt
CMD python iris_flask.py