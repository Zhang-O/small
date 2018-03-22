# -*- coding:utf-8 -*-
# Filename: try.py
# Author：zhang
# Date: 2018/1/30 22:41

import numpy as np
from matplotlib import pyplot as plt


x = np.linspace(-10, 10, 100)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(5, 2, 1)
ax.plot(x, y)
ax.grid()
ax.set(xlabel="xxxxx", ylabel="yyyyy", title="test")

bx = fig.add_subplot(5, 2, 2)
bx.plot(x, np.log(x), 'o-')

cx = fig.add_subplot(5, 2, 3)
cx.plot(x, np.log(x), '.-')

dx = fig.add_subplot(5, 2, 4)
dx.plot(x, np.log(x))

ex = fig.add_subplot(5, 2, 5)
ex.plot(x, np.log(x))

fx = fig.add_subplot(5, 2, 6)
fx.plot(x, np.log(x))

gx = fig.add_subplot(5, 2, 7)
gx.plot(x, np.log(x))

hx = fig.add_subplot(5, 2, 8)
hx.plot(x, np.log(x))

ix = fig.add_subplot(5, 2, 9)
ix.plot(x, np.log(x))

jx = fig.add_subplot(5, 5, 10)
jx.plot(x, np.log(x))


# plt.cla()
plt.show()
