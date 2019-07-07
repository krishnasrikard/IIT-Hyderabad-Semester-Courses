import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('16_14(x).dat',dtype= 'float')
#x = np.linspace(0.5,5,100)
y = np.sqrt(2*x + 1)-np.sqrt(2*x - 1) -1

plt.plot(x,y)
plt.plot(5.0/8,0,'o')
plt.grid()
plt.text(5.0/8 + 0.1,0,'P')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()
