import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x = np.linspace(0,0.25*np.pi,100)
z = np.linspace(0.25*np.pi,0.5*np.pi,100)
t = np.linspace(0.5*np.pi,0.75*np.pi,100)
s = np.linspace(0.75*np.pi,np.pi,100)

y = np.sin(x)**4 + np.cos(x)**4
u = np.sin(z)**4 + np.cos(z)**4
v = np.sin(t)**4 + np.cos(t)**4
w = np.sin(s)**4 + np.cos(s)**4

plt.plot(x,y)
fill_between(z,u,facecolor='orange')
plt.plot(t,v)
fill_between(s,w,facecolor='orange')
plt.grid()
plt.xlabel('$0 < x < \pi$')
plt.ylabel('$\sin^4(x) + \cos^4(x)$')
plt.show()
