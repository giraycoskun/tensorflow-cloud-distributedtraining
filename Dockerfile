FROM tensorflow/tensorflow:latest-gpu

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir -p /giraycoskun/data/mnist/0.0.1/

COPY *.py ./giraycoskun/
 
WORKDIR /giraycoskun