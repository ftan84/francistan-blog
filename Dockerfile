FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /francistanblog
WORKDIR /francistanblog
ADD requirements.txt /francistanblog/
RUN pip install -r requirements.txt
ADD . /francistanblog/
