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
	
t = np.linspace(-np.pi,np.pi,100)
r = 1
x = r*np.cos(t)
y = r*np.sin(t) - 6

plt.figure(1)
plt.axis('equal')
plt.plot(x,y,label = 'Given circle')

t = np.linspace(-1.5,1.5,100)
x = 2*t**2
y = 4*t

plt.plot(x,y,label = 'Given parabola')

O = np.array([0,-6])
P = np.array([2,-4])

line(O,P)
OP = np.linalg.norm(O-P)

t = np.linspace(-np.pi,np.pi,100)
r = OP
x = r*np.cos(t) + 2
y = r*np.sin(t) - 4

plt.plot(x,y,label = 'Required circle')
plt.figure(1)
point(P,'P',0.2,0.1)
point(O,'O',-0.64,-0.64)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.legend()
plt.figure(2)
plt.plot(t,OP)
plt.grid()
plt.xlabel('$t$')
plt.ylabel('OP')
plt.show()
