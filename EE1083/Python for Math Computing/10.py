import numpy as np
import matplotlib.pyplot as plt

def line(a,b):
	m = (b[1]-a[1])/(b[0]-a[0])
	c = a[1]-m*a[0]
	x = np.linspace(a[0],b[0],100)
	y = m*x + c
	plt.plot(x,y, label = '$PQ$')
	
P = np.transpose(np.array([2,1]))
Q = P-2*np.sqrt(3)*np.cos(0.25*np.pi)*np.transpose(np.array([1,1]))
line(P,Q)
plt.plot(P[0],P[1],'o')
plt.plot(Q[0],Q[1],'o')
plt.text(P[0],P[1] - 0.3, 'P')
plt.text(Q[0]-0.3,Q[1], 'Q')
plt.ylim(-5,2)
plt.xlim(-3,4)

x = np.linspace(Q[0],P[0])
y = x-4
plt.plot(x,y,label = '$x - y =4$')
y = 3 - 2*np.sqrt(6) - x
plt.plot(x,y,label = '$x + y =c$')
plt.grid()
plt.legend()
plt.axis('equal')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()
