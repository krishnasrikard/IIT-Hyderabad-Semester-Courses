import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,100)
r = 8.0/3.0
x = r*np.cos(t)
y = -13.0/3.0 + r*np.sin(t)
plt.plot(x,y)
plt.grid()
plt.axis('equal')
plt.axis([-4,3,-7,-1])

x = np.linspace(-4,0,100)

plt.legend(loc=1,prop={'size':8})
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(0,-13.0/3.0,'o')
plt.text(0,-4,'O')
plt.show()
