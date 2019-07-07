import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2*np.pi,100)
x = 6*np.cos(t) + 4
y = 6*np.sin(t) + 4

plt.axis('equal')
plt.plot(x,y,label = 'Circle')

x = np.linspace(-3,12,100)
y1 = ((x-4)**2)/20 - 1
y2 = 5 - ((x-4)**2)/2

plt.plot(x,y1,label = 'Locus 1')
plt.plot(x,y2,label = 'Locus 2')

plt.axis([-5,12,-5,10])
plt.grid()
plt.legend(loc = 3)
plt.show()
