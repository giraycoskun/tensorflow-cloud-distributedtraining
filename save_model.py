import boto3

# Create an S3 access object
s3 = boto3.client("s3")

filename = "./saved_model/saved_model.pb"
bucket = "skyloop-artifacts"
object_name = "mnsit/prediction/saved_model.pb"

response = s3.upload_file(filename, bucket, object_name)
print(response)