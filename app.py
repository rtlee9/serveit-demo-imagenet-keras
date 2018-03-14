"""Serve Keras DenseNet121 model trained on ImageNet.

Prediction endpoint, served at `/predictions` takes a URL pointing to an image
and returns a list of class probabilities.
"""
from serveit.server import ModelServer
from serveit.utils import get_bytes_to_image_callback

from keras.applications.densenet import DenseNet121
from keras.applications.densenet import decode_predictions
from keras.applications.densenet import preprocess_input

from flask import request
import requests

# load DenseNet121 model pretrained on ImageNet
model = DenseNet121(weights='densenet121_weights_tf_dim_ordering_tf_kernels.h5')


# define a loader callback for the API to fetch the relevant data and
# preprocessor callbacks to map to a format expected by the model
def loader():
    """Load image from URL, and preprocess for densenet."""
    url = request.args.get('url')  # read image URL as a request URL param
    response = requests.get(url)  # make request to static image file
    return response.content

# get a bytes-to-image callback, resizing the image to 224x224 for ImageNet
bytes_to_image = get_bytes_to_image_callback(image_dims=(224, 224))

# deploy model to a ModelServer
server = ModelServer(
    model,
    model.predict,
    data_loader=loader,
    preprocessor=[bytes_to_image, preprocess_input],
    postprocessor=decode_predictions,
)

# get flask app for gunicorn serving
app = server.get_app()

if __name__ == '__main__':
    server.serve()
