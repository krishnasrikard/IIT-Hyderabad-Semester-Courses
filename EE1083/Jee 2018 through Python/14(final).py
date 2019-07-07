import numpy as np
import matplotlib.pyplot as plt


x = np.loadtxt('14(x).dat',dtype= 'float')
y = np.loadtxt('14.dat',dtype= 'float')

plt.plot(x,y)
plt.grid()

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(9,-3.0,'o')
plt.text(9,-4,'O')
plt.show()
