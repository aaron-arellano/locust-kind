# build docker file and use latest locust file as base
FROM locustio/locust

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /src
COPY /src .