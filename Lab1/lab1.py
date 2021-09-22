# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:23:01 2021

@author: aryan garg
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt")
plt.plot(data)
plt.show()