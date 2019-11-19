# Table of Contents

* [Basic Classification - Fashion MNIST](#Basic-Classification-Fashion-MNIST)

# Basic Classification - Fashion MNIST

```python
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist

#testing and training data
#can write in this way cuz of keras form of output
(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#scaling values to [0,1]
train_images = train_images/255.0
test_images = test_images/255.0

plt.imshow(train_images[7], cmap=plt.cm.binary)
#cmap makes the image black and white
plt.show()
```

Terminal output:
![](https://github.com/ezhentan/schoolprojects/blob/master/Basic%20Tensorflow/Images/pullover.png)
