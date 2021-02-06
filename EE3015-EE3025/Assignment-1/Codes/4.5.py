import numpy as np
import matplotlib.pyplot as plt

def H(z):
	Num = np.polyval([1,0,1],pow(z,-1))
	Den = np.polyval([0.5,1],pow(z,-1))
	return Num/Den
	
w = np.linspace(-10,10,1000,endpoint=True)
z = np.exp(1j * w)
H = H(z)

plt.figure()
plt.grid()
plt.plot(w,np.abs(H))
plt.xlabel(r'$\omega$')
plt.ylabel(r'$|H(e^{j\omega}|$')
plt.title("Filter Frequency Response")
plt.show()
