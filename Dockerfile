FROM python:3.11-slim

WORKDIR /usr/src/app

RUN apt update
RUN apt install python3 -y
RUN apt-get install -y python3-pip

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "app.py"]
