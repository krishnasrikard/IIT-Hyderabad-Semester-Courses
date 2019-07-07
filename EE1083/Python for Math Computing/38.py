import numpy as np
import matplotlib.pyplot as plt

def point(P,T,O1,O2):
	plt.plot(P[0],P[1],'o')
	plt.text(P[0]+O1,P[1]+O2,T)

def f(x):
	return x**2 + ((1 - 2*x)**2)/np.pi

x = np.linspace(0,1,20)

plt.plot(x,f(x))

x = 2/(np.pi + 4)
P = np.array([x,f(x)])
r = (1 - 2*x)/np.pi

point(P,'P',0,0.03)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$A$')
plt.show()	
	
