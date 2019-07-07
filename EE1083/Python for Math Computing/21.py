import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2,1],[7,-1]])
B = np.transpose(np.array([1,-1]))
print np.dot(np.linalg.inv(A),B)

x = np.linspace(-3,3,10)
z = 7*x + 1

plt.plot(x,z,label = 'Surface')

x = np.linspace(-3,0,5)
y = 1 - 2*x
w = 41*x/38 + 1
plt.plot(x,y,label = 'Incident')
plt.plot(x,w,label = 'Reflected')
plt.grid()
plt.axis('equal')
plt.axis([-5,5,-5,5])
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.show()
