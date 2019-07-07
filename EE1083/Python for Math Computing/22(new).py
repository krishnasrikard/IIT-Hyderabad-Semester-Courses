import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,20,500)
y1 = 2*np.sqrt(x)
y2 = -2*np.sqrt(x)

plt.axis('equal')
plt.plot(x,y1)
plt.plot(x,y2)
plt.grid()

temp = np.sqrt(2)*np.linspace(0.2,1.2,6)
for i in range(0,6):
	t = temp[i]
	P = np.array([t**2,2*t])
	if i == 5:
		plt.plot(P[0],P[1],'o')
		plt.text(P[0] + 0.2,P[1]+1,'P')
	else:
		plt.plot(P[0],P[1],'o')
		y = 2*t - t*(x - t**2)
		plt.plot(x,y)
		
t1 = -2*np.sqrt(2)
Q = np.array([t1**2,2*t1])
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]-1,Q[1]-2.5,'Q')
plt.show()
