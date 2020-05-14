# License
'''
Code by Krishna Srikar Durbha
May 14,2020
Released under GNU GPL
'''

import numpy as np  
import matplotlib.pyplot as plt
import subprocess
import shlex

Data1 = np.loadtxt('ee18btech11014_a.dat')

plt.figure(figsize=(8.0,10.0))
plt.plot(Data1[:,0],Data1[:,1])  
plt.grid()
plt.xlabel("Time")
plt.ylabel("Closed-Loop System Response")
plt.title('Spice Simulation for System with Phase-Margin=72 for DC Signal as Input')

plt.savefig('../../figs/ee18btech11014/ee18btech11014_Spice_Result_PM=72.pdf')
plt.savefig('../../figs/ee18btech11014/ee18btech11014_Spice_Result_PM=72.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11014/ee18btech11014_Spice_Result_PM=72.pdf"))
#plt.show()
