import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()

# 16777216 - because 24 bits color pixels = 2^24
X_valid, X_train = X_train_full[:5000] / 16777216., X_train_full[5000:] / 16777216.
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
X_test = X_test / 16777216

