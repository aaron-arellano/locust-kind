# build docker file and python as base image
FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /locust-kind
COPY . /locust-kind

# validations part of build
RUN black . --check

#needed to load locust file
WORKDIR /locust-kind/locust