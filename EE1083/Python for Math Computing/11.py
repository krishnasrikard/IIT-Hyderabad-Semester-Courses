import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,100)
r = 2
x = -2 + r*np.cos(t)
y = 2 + r*np.sin(t)
plt.plot(x,y)
plt.grid()
plt.axis('equal')
plt.axis([-4,0,0,4])

x = np.linspace(-4,0,100)
y1 = (6 - 4*x)/5
y2 = (10 + 2*x)/3
y3 = 0.75*(1-x)
y4 = -(4 + 5*x)/2

plt.plot(x,y1,label = '$5y + 4x - 6 = 0$')
plt.plot(x,y2,label = '$3y - 2x - 10 = 0$')
plt.plot(x,y3,label = '$4y + 3x - 3 = 0$')
plt.plot(x,y4,label = '$2y + 5x + 4 = 0$')

plt.legend(loc=1,prop={'size':8})
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(-2,2,'o')
plt.text(-2,1.75,'O')
plt.show()
