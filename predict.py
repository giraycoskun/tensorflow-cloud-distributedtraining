import tensorflow_datasets as tfds
import tensorflow as tf
import numpy as np

from PIL import Image
import PIL.ImageOps    

import boto3

s3 = boto3.client("s3")

key = "mnsit/test/test.jpeg"
filename = "data/predict/test.jpeg"

s3.download_file(
        Bucket="skyloop-artifacts", Key=f"{key}", Filename=filename
    )

img = Image.open(filename).convert('L')
img.load()
img = PIL.ImageOps.invert(img)
data = np.asarray( img, dtype="int32")

data = data / 255.0
inputImg = np.expand_dims(data,0).astype(np.float32)

path = 'saved_model/'
model = tf.keras.models.load_model(path)

prediction = model.predict(inputImg)

print(prediction)