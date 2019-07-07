import numpy as np
import matplotlib.pyplot as plt

a = np.sqrt(2)*np.array([1,-1,1,-1])
b = np.array([1,1,-1,1]) + np.sqrt(3)*np.array([-1,1,1,-1])
t = ord('a')
x1 = np.linspace(0,1,100)
x2 = np.linspace(1,np.sqrt(2),100)
x3 = np.linspace(np.sqrt(2),5,100)

for i in range (0,4):
	y1 = 2*(x1**2)/a[i]
	y2 = np.ones(100)*a[i]
	y3 = (2*(b[i]**2) - 4*b[i])/(x3**3)
	plt.figure(i)
	plt.plot(x1,y1)
	plt.plot(x2,y2)
	plt.plot(x3,y3)
	plt.grid()
plt.show()
