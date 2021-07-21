# build docker file and python as base image
FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /locust/src
COPY . /locust

# validations part of build
RUN black . --check
