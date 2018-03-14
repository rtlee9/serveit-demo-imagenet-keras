# Live ServeIt demo
## ImageNet classifier API with Keras pre-trained model

[ServeIt](https://github.com/rtlee9/serveit) is an open source library that lets you serve model predictions and supplementary information from a RESTful API on any domain using your favorite Python ML library in as little as one line of code. This repository illustrates the process of deploying a pre-trained ImageNet classifier with ServeIt to a new API endpoint. The classifier accepts an image URL as a parameter in a POST request and responds with the top predicted classes for that image.

Give it a try!

![cat picture](img/cat.jpg)
```bash
curl -XPOST https://imagenet-keras.ryanlee.io/predictions?url=https://images.pexels.com/photos/96938/pexels-photo-96938.jpeg
# [[["n02123045", "tabby", 0.69397], ["n02123159", "tiger_cat", 0.14688], ["n02124075", "Egyptian_cat", 0.05430], ...]]
```

![plane picture](img/airplane.jpg)
```bash
curl -XPOST https://imagenet-keras.ryanlee.io/predictions?url=https://images.pexels.com/photos/67807/plane-aircraft-take-off-sky-67807.jpeg
# [[["n02690373", "airliner", 0.60765], ["n04592741", "wing", 0.22114], ["n04552348", "warplane", 0.14071], ...]]
```

Please consider buying me a coffee to help cover hosting costs:

<a href="https://www.buymeacoffee.com/6Ii7vzL" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
