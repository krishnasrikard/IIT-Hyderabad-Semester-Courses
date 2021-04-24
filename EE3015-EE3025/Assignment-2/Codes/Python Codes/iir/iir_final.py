import numpy as np
import matplotlib.pyplot as plt
from para import *
from lp_stable_cheb import lp_stable_cheb
from lpbp import lpbp
from bilin import bilin

# IIR  FILTER DESIGN USING THE CHEBYSCHEV APPROXIMATION
# The order of the filter is N = 4


# Getting values of the various analog and digital filter parameters
# The chebyschev filter parameter (epsilon) obtained
# from the given constraints

epsilon = 0.4

# The analog lowpass filter
[p,G_lp] = lp_stable_cheb(epsilon,N)

Omega_L = np.arange(-2,2.01,0.01)
H_analog_lp = G_lp*np.abs(np.divide(1,np.polyval(p,1j*Omega_L)))
# plot(Omega_L,H_analog_lp)
# xlabel('\Omega')
# ylabel('|H_{a,LP}(j\Omega)|')

# The analog bandpass filter
[num,den,G_bp] = lpbp(p,Omega_0,B,Omega_p1)

Omega = np.arange(-0.65,0.66,0.01)
H_analog_bp = G_bp*np.abs(np.divide(np.polyval(num,1j*Omega),np.polyval(den,1j*Omega)))
# plot(Omega,H_analog_bp)
# xlabel('\Omega')
# ylabel('|H_{a,BP}(j\Omega)|')

# The digital bandpass filter
[dignum,digden,G] = bilin(den,omega_p1)

omega = np.arange(-2*np.pi/5,2*np.pi/5 + np.pi/1000, np.pi/1000)
H_dig_bp = G*np.abs(np.divide(np.polyval(dignum,np.exp(-1j*omega)), np.polyval(digden,np.exp(-1j*omega))))

plt.figure()
plt.plot(omega/np.pi,H_dig_bp)
plt.xlabel(r'$\omega/\pi$')
plt.ylabel(r'$|H_{d,BP}(\omega)|$')
plt.show()
iir_num = G*dignum
iir_den = digden

# save iir_num.dat iir_num -ascii
# save iir_den.dat iir_den -ascii

np.savetxt("dignum.dat",dignum)
np.savetxt("digden.dat",digden)
# save digden.dat digden -ascii
# save G.dat G -ascii
