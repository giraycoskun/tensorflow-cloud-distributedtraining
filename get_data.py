import boto3

# Create an S3 access object
s3 = boto3.client("s3")

key_list = [
    "mnsit/input/mnist-train.tfrecord-00000-of-00001",
    "mnsit/input/mnist-test.tfrecord-00000-of-00001",
    "mnsit/input/image.image.json",
    "mnsit/input/dataset_info.json"
]

for key in key_list:
    filename = key.split('/')[-1]
    s3.download_file(
        Bucket="skyloop-artifacts", Key=f"{key}", Filename=f"data/mnist/3.0.1/{filename}"
    )
    print(key)
    #print(filename)