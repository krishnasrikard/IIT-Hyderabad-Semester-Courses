import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,100)
r = (np.sqrt(2) + 1)/8
x = r*np.cos(t)
y = r*np.sqrt(2) + r*np.sin(t)
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


plt.legend(loc=1,prop={'size':8})
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(0,r,'o')
plt.text(0,0.5,'O')
plt.show()
