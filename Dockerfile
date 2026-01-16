FROM python:3.10-slim-bookworm

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y ffmpeg git && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip

COPY . /app/
WORKDIR /app/

# Pehle dependencies install karte hain jo error deti hain
RUN pip3 install --no-cache-dir ntgcalls==2.0.6
RUN pip3 install --no-cache-dir pytgcalls==2.1.0

# Baaki bachi hui requirements
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD ["python3", "main.py"]
