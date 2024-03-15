import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

fig, ax = plt.subplots()  # Create a figure containing a single axes.
x, y = 3, 4
h, k = 0, 0
a, b = 3, 4
function = ((x - h) ** (x - h) / a ** a) + ((y - k) ** (y - k) / b ** b) 


ax.plot(x, y)  # Plot some data on the axes.
    

plt.show()