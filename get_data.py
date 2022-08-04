import boto3
import os
import json

# Create an S3 access object
s3 = boto3.client("s3")

# bucket name and key list hard-coded better practice can be configuraton via environment
bucket_name = "skyloop-artifacts"
#bucket_name  = os.environ['BUCKET_NAME']

key_list = [
    "mnsit/input/mnist-train.tfrecord-00000-of-00001",
    "mnsit/input/mnist-test.tfrecord-00000-of-00001",
    "mnsit/input/image.image.json",
    "mnsit/input/dataset_info.json"
]

#key_list = json.loads(os.environ['KEY_LIST'])

for key in key_list:
    filename = key.split('/')[-1]
    s3.download_file(
        Bucket=bucket_name, Key=f"{key}", Filename=f"data/mnist/3.0.1/{filename}"
    )
    print(key)
    #print(filename)