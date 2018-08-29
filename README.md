# Live ServeIt demo
## ImageNet classifier API with Keras pre-trained model

[ServeIt](https://github.com/rtlee9/serveit) is an open source library that lets you serve model predictions and supplementary information from a RESTful API on any domain using your favorite Python ML library in as little as one line of code. This repository illustrates the process of deploying a pre-trained ImageNet classifier with ServeIt to a new API endpoint. The classifier accepts an image URL as a parameter in a POST request and responds with the top predicted classes for that image.

Give it a try!

![cat picture](img/cat.jpg)
```bash
curl -XPOST 'https://imagenet-keras.ryanlee.io/predictions?url=https://cdn.pixabay.com/photo/2017/11/14/13/06/kitty-2948404_640.jpg'
# [[["n02123159", "tiger_cat", 0.590599775314331], ["n03942813", "ping-pong_ball", 0.08682757616043091], ["n02119789", "kit_fox", 0.07293993979692459]]]
```

![plane picture](img/airplane.jpg)
```bash
curl -XPOST 'https://imagenet-keras.ryanlee.io/predictions?url=https://cdn.pixabay.com/photo/2012/06/28/08/26/plane-50893_640.jpg'
# [[["n02690373", "airliner", 0.5754486322402954], ["n04592741", "wing", 0.2601102292537689], ["n04552348", "warplane", 0.12749212980270386]]]
```

Please consider buying me a coffee to help cover hosting costs:

<a href="https://www.buymeacoffee.com/6Ii7vzL" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
