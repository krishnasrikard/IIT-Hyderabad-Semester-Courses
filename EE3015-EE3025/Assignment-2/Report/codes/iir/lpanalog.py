import numpy as np
import matplotlib.pyplot as plt
from cheb import cheb

# The low-pass Chebyschev design parameters
epsilon = 0.4
N = 4

# Analytically obtaining the roots of the Chebyschev polynomial
# in the left half of the complex plane

beta = pow((np.sqrt(1+pow(epsilon,2))+ 1)/epsilon,(1/N))
r1 = (pow(beta,2)-1)/(2*beta)
r2 = (pow(beta,2)+1)/(2*beta)

# Obtaining the polynomial approximation for the low pass
# Chebyschev filter to obtain a stable filter
u = 1
for n in range(int(N/2)):
	phi = np.pi/2 + (2*n+1)*np.pi/(2*N)
	v = np.array([1, -2*r1*np.cos(phi), pow(r1*np.cos(phi),2)+pow(r2*np.sin(phi),2)])
	p = np.convolve(v,u)
	u = p

# The following was to verify that the roots obtained # are correct # roots(p)
p1 = pow(epsilon,2)*np.convolve(cheb(N),cheb(N)) + np.append(np.zeros((2*N,)), np.array([1]))
# r = roots(p1)

# Evaluating the gain of the stable lowpass filter
# The gain has to be 1/sqrt(1+epsilon^2) at Omega = 1
G = np.abs(np.polyval(p,1j))/np.sqrt(1+pow(epsilon,2))

# Plotting the magnitude response of the stable filter and comparing with the desired response for the purpose of verification

Omega = np.arange(0,2.01,0.01)
H_stable = np.abs(np.divide(G,np.polyval(p,1j*Omega)))
H_cheb = np.abs(np.sqrt(np.divide(1,np.polyval(p1,1j*Omega))))

plt.figure()
plt.plot(Omega,H_stable,'o')
plt.plot(Omega,H_cheb)
plt.xlabel(r'$\Omega$')
plt.ylabel(r'$|H_{a,LP}(j\Omega)|$')
plt.title("Chebyshev Low Pass Filter Design")
plt.savefig("../../figs/IIR_ChebyshevDesign.eps")
plt.show()
