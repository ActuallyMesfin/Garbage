import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

fig, ax = plt.subplots()  # Create a figure containing a single axes.
x = 0
y = x + 1

while x < 100:
    print(x)
    ax.plot(x, y)  # Plot some data on the axes.
    x+=1

plt.show()