import numpy as np
import matplotlib.pyplot as plt


x = np.loadtxt('35(x).dat',dtype= 'double')
y = np.loadtxt('35.dat',dtype= 'double')

plt.plot(x,y)
plt.grid()
plt.axis('equal')
plt.axis([-1,1,0,2])

x = np.linspace(-1,1,100)
y1 = x
y2 = -x
y3 = 4*(x**2)

plt.plot(x,y1,label = '$y = x$')
plt.plot(x,y2,label = '$y = -x$')
plt.plot(x,y3,label = '$y = 4x^2$')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(0,0.3,'o')
plt.text(0,0.4,'O')
plt.show()
