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

Data3 = np.loadtxt('ee18btech11014_3.dat')

plt.figure(figsize=(8.0,12.0))
plt.plot(Data3[:,0],Data3[:,1])  
plt.grid()
plt.xlabel("Time")
plt.ylabel("Closed-Loop System Response")
plt.title('Spice Simulation for Unstable System with Step Signal as Input')

plt.savefig('../../figs/ee18btech11014/ee18btech11014_Spice_Result.pdf')
plt.savefig('../../figs/ee18btech11014/ee18btech11014_Spice_Result.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11014/ee18btech11014_Spice_Result.pdf"))
#plt.show()
