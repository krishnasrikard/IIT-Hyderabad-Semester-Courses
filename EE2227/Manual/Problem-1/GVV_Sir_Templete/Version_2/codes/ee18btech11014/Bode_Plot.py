# License
'''
Code by Krishna Srikar Durbha
April 11,2020
Released under GNU GPL
'''
# The Following is written to run in Termux

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# Import the bellow Libraries if running on Termux
import subprocess
import shlex

# Poles
p1 = 1/(2*np.pi*1e5)
p2 = 1/(2*np.pi*1e6)
p3 = 1/(2*np.pi*1e7)

# Numerator and Denominator of Transfer Function
Num = [1e5]
Den = [p1*p2*p3, (p1*p2 + p3*p2 + p1*p3), (p1+p2+p3), 1]

sys = signal.lti(Num, Den)
w, mag, phase = signal.bode(sys)

# Piecewise Linear Plot
def Piecewise(w):
	fmin = np.min(w)/15*np.pi
	fmax = np.max(w)/2*np.pi
	f = np.arange(fmin,fmax,500)
	val = np.zeros(f.shape)
	for i in range(f.shape[0]):
		if (f[i] <= 1e5):
			val[i] = 100
		elif (f[i] > 1e5 and f[i] <= 1e6):
			val[i] = 200-20*np.log10(f[i])
		elif (f[i] > 1e6 and f[i] <= 1e7):
			val[i] = 320-40*np.log10(f[i])
		else:
			val[i] = 460-60*np.log10(f[i])
	return val,f
pmag,freq = Piecewise(w)

# Bode Magnitude Plot
plt.figure(figsize=(8.0,10.0))
plt.subplot(2,1,1)
plt.title("Magnitude Bode Plot")
plt.xlabel('f (in Hz)')
plt.ylabel('$20\log|G(f)|$')
plt.grid(which='both')
# Plotting with 'f' on x-axis
plt.semilogx(w/(2*np.pi), mag)
plt.semilogx(freq, pmag)

# Bode Phase Plot
plt.subplot(2,1,2)
plt.title("Phase Bode Plot")
plt.xlabel('f (in Hz)')
plt.ylabel('Phase of G(f)')
plt.grid(which='both')
# Plotting with 'f' on x-axis
plt.semilogx(w/(2*np.pi), phase)

plt.savefig('../../figs/ee18btech11014/Bode_Plot.eps')
plt.savefig('../../figs/ee18btech11014/Bode_Plot.pdf')

''' If using Termux '''
subprocess.run(shlex.split("termux-open ./figs/ee18btech11014/Bode_Plot.pdf"))
#plt.show()



