import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1,1.2,100)
x = 4*t**2 + 3
y = 8*t**3 - 1
z = 3*(x-7) + 7
plt.plot(x,y,label = 'curve , $x=4t^2+3 ,y=8t^3-1$')
plt.plot(x,z,label = 'tangent , $y-7=3(x-7)$')
plt.grid()
plt.legend(loc='best' ,prop={'size':11})

A = np.array([7, 4])
B = np.array([7, -2])

plt.plot(A,B,'o')
for xy in zip(A,B):
	plt.annotate('(%s, %s)' %xy, xy=xy, xytext=(30,0), textcoords='offset points')
	
plt.text(7,8,'P')
plt.text(4,-4,'Q')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()
