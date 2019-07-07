import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,1000)
y =4 + 0.5*(np.sin(2*x))**2-2*(np.cos(x))**4
plt.plot(x,y)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()
