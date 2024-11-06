# api/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN apt -y update && apt -y upgrade
RUN apt -y install libopencv-dev

CMD ["python", "app.py"]
