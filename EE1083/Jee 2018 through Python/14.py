import numpy as np
import matplotlib.pyplot as plt

plt.axis([0,20,-10,20])

x2 = np.linspace(0,9,100)
x1 = np.linspace(9,20,100)

y = x1 -4*(np.sqrt(x1))
z = x2 + 12 - 8*(np.sqrt(x2))

plt.plot(x1,y, label = '$f(x) = x - 4*(x)^0.5$')
plt.plot(x2,z, label = '$f(x) = x - 8*(x)^0.5 + 12$')

sol = np.zeros((2,1))
sol[0] = 9
sol[1] = -3

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
