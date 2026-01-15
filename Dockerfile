FROM python:3.10-slim-buster

RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg-y
RUN pip3 install -U pip

COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt

CMD ["python3", "main.py"]
