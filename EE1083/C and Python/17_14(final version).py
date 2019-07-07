import numpy as np
import matplotlib.pyplot as plt


x = np.loadtxt('17_14(x).dat',dtype= 'float')
y = np.loadtxt('17_14(remodified).dat',dtype= 'float')

plt.plot(x,y)
plt.grid()

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(0,-13.0/3.0,'o')
plt.text(0,-4,'O')
plt.show()
