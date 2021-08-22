# syntax=docker/dockerfile:1

FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8080:8080
COPY . .
# get wget
RUN apt-get update && apt-get install -y wget

# Install justext
RUN wget http://corpus.tools/raw-attachment/wiki/Downloads/justext-3.0.tar.gz && \
    tar xzvf justext-3.0.tar.gz && \
    cd justext-3.0/ && \
    python3 setup.py install --user


CMD ["python3", "main.py"]