import numpy as np
import matplotlib.pyplot as plt
x = 1e3
a = np.linspace(0,2,100)
y = (1+ a/x - 4/x**2)**(2*x)
z = ((np.exp(3)))*np.ones(100)
bx=plt.plot(a,z, label = 'e^3')
plt.plot(a,y, label = 'Limit_value')

sol = np.zeros((2,1))
sol[0] = 3.0/2.0
sol[1] = np.exp(3)

A = np.around(sol[0],decimals=2)
B = np.around(sol[1],decimals=2)

plt.plot(A,B,'o')
for xy in zip (A,B):
	plt.annotate('(%s, %s)' %xy,xy=xy,xytext=(30,0),textcoords='offset points')
		
plt.grid()
plt.legend([bx[0]],['$e^3$'], loc='best' ,prop={'size':11})
plt.xlabel('$a$')
plt.ylabel('$\\left(1 + \\frac{a}{x} - \\frac{4}{x^2}\\right)^{2x}$')
plt.show()
