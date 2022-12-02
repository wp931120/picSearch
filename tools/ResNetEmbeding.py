import numpy as np
import os
import requests
from PIL import Image
import io

import tensorflow as tf
print(tf.__version__)

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


class ResNetEmbeding:
    def __init__(self, path):
        self.model = tf.keras.applications.ResNet50(include_top=False,weights=None)
        self.load_model(path)

    def load_model(self, path):
        self.model.load_weights(path)

    def extract_feature(self, url, distant=True):
        if distant:
            content = requests.get(url, stream=True).content
            byteStream = io.BytesIO(content)
            image = Image.open(byteStream)
        else:
            image = Image.open(url)
        image = image.resize([224, 224]).convert('RGB')
        y = tf.keras.preprocessing.image.img_to_array(image)
        y = np.expand_dims(y, axis=0)
        y = tf.keras.applications.resnet50.preprocess_input(y)
        y = self.model(y)
        result = tf.keras.layers.GlobalAveragePooling2D()(y)
        feature = [x for x in result.numpy()[0].tolist()]
        return feature


if __name__ == '__main__':
    resnet = ResNetEmbeding("../model/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5")
    resnet.extract_feature("http://localhost:9000/picture/ILSVRC2012_img_val/ILSVRC2012_val_00044293.JPEG")