# syntax=docker/dockerfile:1

FROM python:3.10-rc-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8080:8080
COPY . .
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]