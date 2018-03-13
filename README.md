# Live ServeIt demo
## ImageNet classifier API with Keras pretrained model

[ServeIt](https://github.com/rtlee9/serveit) lets you easily serve model predictions and supplementary information from a RESTful API. This repository illustrates this process by deploying a pretrained ImageNet classifier to an API endpoint. The classifier accepts an image URL as a URL argument in a GET request and responds with the top 3 predicted classes for that image.

Give it a try!

![cat picture](img/cat.jpg)
```bash
curl -XPOST https://imagenet-keras.ryanlee.io/predictions?url=https://images.pexels.com/photos/96938/pexels-photo-96938.jpeg
# [["n02123045", "tabby", 0.693970263004303], ["n02123159", "tiger_cat", 0.1468803733587265], ["n02124075", "Egyptian_cat", 0.054300565272569656]]
```

![plane picture](img/airplane.jpg)
```bash
curl -XPOST https://imagenet-keras.ryanlee.io/predictions?url=https://images.pexels.com/photos/67807/plane-aircraft-take-off-sky-67807.jpeg
# [["n02690373", "airliner", 0.6076506972312927], ["n04592741", "wing", 0.221147820353508], ["n04552348", "warplane", 0.14071764051914215]]
```
