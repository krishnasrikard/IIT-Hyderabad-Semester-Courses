import numpy as np
import matplotlib.pyplot as plt
import os
def File2Numpy(Path):
	Content = []
	for i in open(Path).readlines():
		Content.append(i.strip().split())
		
	Content = np.array(Content).astype(float)
	x = Content[:,1]
	y = Content[:,3]
	return np.array([x,y]).T
Path = "../Data/5b/"
DataFiles = len(os.listdir(Path))
# Load Resistance
R = np.arange(10,110,10) * 1000
# Gain
Gain, PeakGain, Vm = [], [], []
# Reading Files
for i in range(DataFiles):
	Gain.append(File2Numpy(Path+str(i+1)+".dat"))
Gain = np.array(Gain)
# Plotting Gain as function VG
plt.figure(figsize=(7,7))
for i in range(Gain.shape[0]):
	PeakGain.append(np.min(Gain[i,:,1]))
	ind = np.argmin(Gain[i,:,1])
	Vm.append(Gain[i,ind,0])
	plt.plot(Gain[i,:,0],Gain[i,:,1], label=str(int(R[i]/1000))+"K ohm")
plt.legend()
plt.grid()
plt.title(r"Gain vs $V_G$")
plt.xlabel(r"$V_G$")
plt.ylabel("Gain")
plt.savefig("5b_Gain.png")
# Plotting Peak Gain
plt.figure(figsize=(7,7))
plt.plot(R,PeakGain)
plt.grid()
plt.title(r"PeakGain vs R")
plt.xlabel("R")
plt.ylabel("PeakGain")
plt.savefig("5b_PeakGain.png")
# Plotting Vm
plt.figure(figsize=(7,7))
plt.plot(R,Vm)
plt.grid()
plt.title(r"Vm vs R")
plt.xlabel("R")
plt.ylabel("Vm")
plt.savefig("5b_Vm.png")
plt.show()
