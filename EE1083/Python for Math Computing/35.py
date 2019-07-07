import numpy as np
import matplotlib.pyplot as plt

def line(a,b):
	m = (b[1]-a[1])/(b[0]- a[0])
	c = a[1]-m*a[0]
	x = np.linspace(a[0],b[0],100)
	y=m*x + c
	plt.plot(x,y)
	
def point(P,T,O1,O2):
	plt.plot(P[0],P[1],'o')
	plt.text(P[0]+O1,P[1]+O2,T)

t = np.linspace(0,2*np.pi,100)
x = 5*np.cos(t) + 2
y = 5*np.sin(t) - 3

plt.axis('equal')
plt.plot(x,y)

y = x - 5

plt.plot(x,y)

S = np.array([-3,2])
O = np.array([2,-3])

point(S,'S',-1,0.1)
point(O,'O',0.45,-0.5)
line(O,S)

t = np.linspace(0,2*np.pi,100)
r = 5*np.sqrt(3)
x = r*np.cos(t) - 3
y = r*np.sin(t) + 2

plt.plot(x,y)
plt.grid()
plt.show()
