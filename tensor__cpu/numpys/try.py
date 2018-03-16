import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    z[z < 0] = 0
    return z
