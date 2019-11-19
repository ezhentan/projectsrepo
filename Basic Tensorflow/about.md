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
(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#scaling values to [0,1], both sets should be pre-processed the same way
train_images = train_images/255.0
test_images = test_images/255.0

plt.imshow(train_images[7], cmap=plt.cm.binary)
#cmap binary makes the image black and white
plt.show()
```

Terminal output:
![](https://github.com/ezhentan/schoolprojects/blob/master/Basic%20Tensorflow/Images/pullover.png)

```python
#Verifying data from training set
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()
```

Terminal output:
![](https://github.com/ezhentan/schoolprojects/blob/master/Basic%20Tensorflow/Images/25_images.png)

Sources:

Tensorflow (n.d.). Basic classification: Classify images of clothing. Retrieved from: https://www.tensorflow.org/tutorials/keras/classification#import_the_fashion_mnist_dataset

freeCodeCamp.org (2019, September 26). TensorFlow 2.0 Full Tutorial - Python Neural Networks for Beginners. Retrieved from: https://www.youtube.com/watch?v=6g4O5UOH304&t=3936s
