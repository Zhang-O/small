import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt



x = np.mgrid[-10:10:0.02]
def fourier1():
    s = np.pi / 2

    for i in range(1,100,1):
        s0 = 2 / np.pi * (1 - (-1) ** i) / i ** 2 * np.cos(i * x)
        s = s + s0

        plt.close()

        plt.plot(x, s, 'orange', linewidth=0.6)
        plt.title('fourier1')
        plt.show()





fourier1()