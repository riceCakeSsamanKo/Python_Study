import numpy as np
import random
import matplotlib.pyplot as plt
from keras.datasets import mnist
# load MNIST data (60000 training dataset // 100000 training dataset)
(train_X, train_y), (test_X, test_y) = mnist.load_data()
# Prepare dataset for training (reshape)
X_train = train_X.reshape(60000,784).astype(float)
X_test = test_X.reshape(10000,784).astype(float)
y_train = train_y
y_test = test_y
# Data size
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)
