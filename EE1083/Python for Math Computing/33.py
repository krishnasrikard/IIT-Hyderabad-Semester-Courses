import numpy as np
import matplotlib.pyplot as plt

def line(a,b,s):
	m = (b[1]-a[1])/(b[0]-a[0])
	c = a[1]-m*a[0]
	x = np.linspace(a[0],b[0],100)
	y = m*x + c
	plt.plot(x,y,label = s)
	
def point(P,T,O1,O2):
	plt.plot(P[0],P[1],'o')
	plt.text(P[0]+O1,P[1]+O2,T)
	
A = np.linalg.inv(np.array([[1,-1],[7,-1]]))
B = np.array([-1,5])
P = np.dot(A,B)

A = np.linalg.inv(np.array([[1,2],[1,-1]]))
B = np.array([-5,-1])
Q = np.dot(A,B)

A = np.linalg.inv(np.array([[1,2],[7,-1]]))
B = np.array([-5,5])
S = np.dot(A,B)
R = np.transpose(np.array([-3,-6]))
O = np.transpose(np.array([-1,-2]))
line(P,Q,'$y = x + 1$')
line(S,P,'$y = 7x - 5$')
line(Q,S,'$x + 2y + 5 = 0$')
line(Q,R,'$y = 7x + 15$')
line(R,S,'$y = x - 3$')
point(P,'P',-0.4,0)
point(Q,'Q',-0.5,0)
point(S,'S',0.2,0)
point(O,'O',0.12,0)
point(R,'R',0.2,-0.3)
plt.legend(loc=4)
plt.grid()
plt.show()
