FROM tensorflow/tensorflow:latest-gpu

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir -p /giraycoskun

COPY *.py ./giraycoskun/
 
WORKDIR /giraycoskun