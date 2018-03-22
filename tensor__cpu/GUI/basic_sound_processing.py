# -*- coding: utf-8 -*-
import os
import pylab
import numpy as np
from scipy.io import wavfile
from matplotlib import pyplot as plt
from scipy.fftpack import fft


# Kbps 表示 “每秒千字节数”
os.system("ffmpeg -loglevel panic -y -i ./QT-742440ans.mp3 -ac 2 -ar 16000 ./QT-742440ans2.wav")

sampFreq, snd = wavfile.read('440_sine.wav')

shape = snd.shape
duration = shape[0]

snd = snd / 2.0**15

timeArray = np.arange(0, duration, 1) / sampFreq * 1000


fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
ax.plot(timeArray, snd[:, 0])
ax.grid()
ax.set(xlabel="time", ylabel="c1", title="test")

bx = fig.add_subplot(2, 1, 2)
bx.plot(timeArray, snd[:, 1])
bx.grid()
bx.set(xlabel="time", ylabel="c2", title="test")

p = fft(snd[:, 1])


plt.show()

# pylab.plot(timeArray, snd[:, 0])
# print(timeArray)



