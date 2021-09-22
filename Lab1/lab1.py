# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:23:01 2021

@author: aryan garg
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt")
x = np.array(list(zip(*data))[0])
y = np.array(list(zip(*data))[1])

plt.plot(x, y, 'o')

w, b  = np.polyfit(x,y,deg=1)
line  = w * x + b

plt.plot(x, line, "r--")

plt.show()