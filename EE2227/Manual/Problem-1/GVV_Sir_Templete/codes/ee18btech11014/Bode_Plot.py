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

# Bode Magnitude Plot
plt.figure()
plt.title("Magnitude Bode Plot")
plt.xlabel('f (in Hz)')
plt.ylabel('$20\log|G(f)|$')
plt.grid(which='both')
# Plotting with 'f' on x-axis
plt.semilogx(w/(2*np.pi), mag)
plt.savefig('../../figs/ee18btech11014/Magnitude_Plot.eps')
plt.savefig('../../figs/ee18btech11014/Magnitude_Plot.pdf')

''' If using Termux '''
subprocess.run(shlex.split("termux-open ./figs/ee18btech11014/Magnitude_Plot.pdf"))
#plt.show()

# Bode Phase Plot
plt.figure()
plt.title("Phase Bode Plot")
plt.xlabel('f (in Hz)')
plt.ylabel('Phase of G(f)')
plt.grid(which='both')
# Plotting with 'f' on x-axis
plt.semilogx(w/(2*np.pi), phase)  
plt.savefig('../../figs/ee18btech11014/Phase_Plot.eps')
plt.savefig('../../figs/ee18btech11014/Phase_Plot.pdf')

''' If using Termux '''
subprocess.run(shlex.split("termux-open ./figs/ee18btech11014/Phase_Plot.pdf"))
#plt.show()



