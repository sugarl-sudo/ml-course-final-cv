# api/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN apt -y update && apt -y upgrade
RUN apt -y install libopencv-dev \
    && apt-get install -y cmake build-essential libprotobuf-dev protobuf-compiler 

CMD ["python", "app.py"]
