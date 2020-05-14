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

Data1 = np.loadtxt('ee18btech11014_1.dat')
Data2 = np.loadtxt('ee18btech11014_2.dat')

plt.figure(figsize=(8.0,12.0))
plt.subplot(2,1,1)
plt.plot(Data1[:,0],Data1[:,1])  
plt.grid()
plt.xlabel("Time")
plt.ylabel("Closed-Loop System Response")
plt.title('Spice Simulation for System with Phase-Margin=90 for Step Signal as Input')

plt.subplot(2,1,2)
plt.plot(Data2[:,0],Data2[:,1])  
plt.grid()
plt.xlabel("Time")
plt.ylabel("Closed-Loop System Response")
plt.title('Spice Simulation for System with Phase-Margin=90 for Sinusoidal Signal as Input')

plt.savefig('../../figs/ee18btech11014/ee18btech11014_Spice_Result_PM=90.pdf')
plt.savefig('../../figs/ee18btech11014/ee18btech11014_Spice_Result_PM=90.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11014/ee18btech11014_Spice_Result_90.pdf"))
#plt.show()
