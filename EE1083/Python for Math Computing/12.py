import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,10000)
y1 = np.sqrt(16*((x**2)/9 -1))
y2 = -np.sqrt(16*((x**2)/9 - 1))
plt.plot(x,y1)
plt.plot(x,y2)
plt.grid()
plt.ylabel('$y$')
plt.xlabel('$x$')
plt.show() 
