import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0,2,100)
z = 1 + 1j*a
y = np.imag(z**3)
a_t = np.roots([-1,0,3,0])
print(a_t)
ind = np.nonzero(a_t > 0)
print(ind)
a_v = a_t[ind]
print(a_v)
plt.plot(a,y)
plt.plot(a_v,0,'o')
plt.ylabel('$Im(z)$')
plt.xlabel('$a$')
plt.grid()
plt.show()
