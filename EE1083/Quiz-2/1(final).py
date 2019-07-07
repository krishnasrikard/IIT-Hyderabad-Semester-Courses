import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import *

k = math.exp(2.0/3.0)
t = np.linspace(-4,4,100)
x = np.loadtxt('1(x).dat',dtype= 'double')
y = np.loadtxt('1(y).dat',dtype= 'double')
plt.plot(x,y)


plt.grid()
plt.axis('equal')
plt.axis([-1,k,0,4])

x = np.linspace(0,k,100)
y1 = 1.0/x
y2 = x**2

z = np.minimum(y1,y2)
fill_between(x,z,color='g')

y = np.linspace(0,10,100)
plt.plot(x,y1,label = '$y = 1/x$')

plt.legend(loc=1,prop={'size':8})
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(1,1,'o')
plt.text(1,0.5,'O')
plt.show()
