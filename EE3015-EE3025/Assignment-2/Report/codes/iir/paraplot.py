# PLOTS OF THE LOWPASS CHEBYSCHEV FILTER OF ORDER N AND 0.3184 < epsilon < 0.6197

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")


plt.figure()
for N in range(4,5):
	EpsilonArray = np.round(np.arange(0.35,0.65,0.05),decimals=3)
	Omega = np.arange(0.01,2.01,0.01) + 0*1j
	for i in range(EpsilonArray.shape[0]):
		epsilon = EpsilonArray[i]
		H = np.divide(1, np.sqrt(1 + (pow(epsilon,2) * np.square(np.cosh(N*np.arccosh(Omega))))))
		plt.plot(Omega,H,label=r"$\epsilon = $" + str(epsilon))

plt.grid()
plt.xlabel(r"$\omega$")
plt.ylabel(r"$|H_{a,LP}(j\Omega)|$")
plt.legend()
plt.title("Chebyshev Low Pass Filter for various Epsilon")
plt.savefig("../../figs/IIR_Chebyshev_LowPass.eps")
plt.show()
