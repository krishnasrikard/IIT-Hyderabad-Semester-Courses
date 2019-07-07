import numpy as np
import matplotlib.pyplot as plt

b = -1
x2 = np.linspace(-1,1,100)
x3 = np.linspace(1,2,100)
a = -1 - np.pi/2
y = -x2
z = a + np.arccos(b+(x3))

plt.plot(x3,z, label = '$f(x) =  a + \cos^{-1}(x+b)$')
plt.plot(x2,y, label = '$f(x) = -x$')

sol = np.zeros((2,1))
sol[0] = 1
sol[1] = -1

A = sol[0]
B = sol[1]

plt.plot(A,B,'o')
for xy in zip(A,B):
	plt.annotate('(%s, %s)'%xy,xy=xy,xytext=(30,0), textcoords='offset points')
	
plt.grid()
plt.legend(loc='best' ,prop={'size':11})
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.show()

