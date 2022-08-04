# Guide for Distributed Training on AWS with Tensorflow

- get_data.py &rarr; fetch data from S3 reqires directory configuration (sets at Dockerfile) and S3 Bucket name and key values (file names)

- train.py &rarr; loads data trains a tensorflow model for iamge classification saves model locally

- predict.py &rarr; downloads input file from S3 and predicts by using the model

- save_model.py &rarr; saves model to the S3 bucket requires configuration of S3 Bucket name