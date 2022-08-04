FROM tensorflow/tensorflow:latest-gpu

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir -p /giraycoskun/data/mnist/3.0.1/

RUN mkdir -p /giraycoskun/data/mnist/predict/

COPY *.py ./giraycoskun/

COPY start.sh ./giraycoskun/
 
WORKDIR /giraycoskun