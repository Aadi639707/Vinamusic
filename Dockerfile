FROM python:3.10-slim-bookworm

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip

COPY . /app/
WORKDIR /app/

# Fresh install without using old cache
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD ["python3", "main.py"]
