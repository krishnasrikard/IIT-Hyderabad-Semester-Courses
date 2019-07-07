import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,100)
p = 2*np.sqrt(3)
q = 4
x = p*np.cos(t)
y = q*np.sin(t)
e = np.sqrt(1-(p/q)**2)

plt.plot(x,y)
plt.grid()
plt.axis('equal')
plt.plot(0,q*e,'o')
plt.plot(0,-q*e,'o')
plt.text(0,(q*e)-0.6,'F1')
plt.text(0,(-q*e)+0.2,'F2')

b = 2
a = np.sqrt(5)

x = np.linspace(-4,4,100)
y1 = b*np.sqrt((x/a)**2 + 1)
y2 = -b*np.sqrt((x/a)**2 + 1)

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(np.sqrt(5),2*np.sqrt(2),'o')
plt.plot(np.sqrt(10),2*np.sqrt(3),'o')
plt.plot(5,2*np.sqrt(3),'o')

plt.text(np.sqrt(5),2*np.sqrt(2)-0.55,'A')
plt.text(np.sqrt(10),2*np.sqrt(3)-0.2,'B')
plt.plot(5+0.2,2*np.sqrt(3)-0.2,'C')
plt.show()
