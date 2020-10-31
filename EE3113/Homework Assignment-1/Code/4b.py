#Python Code to Plot Simulation from Data

import numpy as np
import matplotlib.pyplot as plt

def File2Numpy(Path):
	Content = []
	for i in open(Path).readlines():
		Content.append(i.strip().split())
		
	Content = np.array(Content).astype(float)
	x = Content[:,1]
	y = Content[:,3]
	return np.array([x,y]).T
	
# Data of Long Channel N-MOSFET
ln1 = File2Numpy("../Data/4a/nmosl1.dat")
ln2 = File2Numpy("../Data/4a/nmosl2.dat")
ln3 = File2Numpy("../Data/4a/nmosl3.dat")
ln4 = File2Numpy("../Data/4a/nmosl4.dat")

# Data of Long Channel P-MOSFET
lp1 = File2Numpy("../Data/4a/pmosl1.dat")
lp2 = File2Numpy("../Data/4a/pmosl2.dat")
lp3 = File2Numpy("../Data/4a/pmosl3.dat")
lp4 = File2Numpy("../Data/4a/pmosl4.dat")

# Data of Short Channel N-MOSFET
sn1 = File2Numpy("../Data/4a/nmoss1.dat")
sn2 = File2Numpy("../Data/4a/nmoss2.dat")
sn3 = File2Numpy("../Data/4a/nmoss3.dat")
sn4 = File2Numpy("../Data/4a/nmoss4.dat")

# Data of Short Channel P-MOSFET
sp1 = File2Numpy("../Data/4a/pmoss1.dat")
sp2 = File2Numpy("../Data/4a/pmoss2.dat")
sp3 = File2Numpy("../Data/4a/pmoss3.dat")
sp4 = File2Numpy("../Data/4a/pmoss4.dat")

# Transition
a = File2Numpy("../Data/4b/nmosl.dat")
b = File2Numpy("../Data/4b/pmosl.dat")
c = File2Numpy("../Data/4b/nmoss.dat")
d = File2Numpy("../Data/4b/pmoss.dat")

plt.figure(figsize=(20,20))

plt.subplot(2,2,1)
plt.plot(ln1[:,0],ln1[:,1],label=r"$V_{GS}$ = 0.5")
plt.plot(ln2[:,0],ln2[:,1],label=r"$V_{GS}$ = 1")
plt.plot(ln3[:,0],ln3[:,1],label=r"$V_{GS}$ = 1.5")
plt.plot(ln4[:,0],ln4[:,1],label=r"$V_{GS}$ = 2")
plt.plot(a[:,0],a[:,1],label=r"$V_{GS} - V_{Th}$")
plt.title("Long Channel NMOS")
plt.grid()
plt.legend()
plt.xlabel(r"$V_{D}$")
plt.ylabel(r"$I_{D}$")

plt.subplot(2,2,2)
plt.plot(lp1[:,0],lp1[:,1],label=r"$V_{GS}$ = -0.5")
plt.plot(lp2[:,0],lp2[:,1],label=r"$V_{GS}$ = -1")
plt.plot(lp3[:,0],lp3[:,1],label=r"$V_{GS}$ = -1.5")
plt.plot(lp4[:,0],lp4[:,1],label=r"$V_{GS}$ = -2")
plt.plot(b[:,0],b[:,1],label=r"$V_{GS} - V_{Th}$")
plt.title("Long Channel PMOS")
plt.grid()
plt.legend()
plt.xlabel(r"$V_{D}$")
plt.ylabel(r"$I_{D}$")

plt.subplot(2,2,3)
plt.plot(sn1[:,0],sn1[:,1],label=r"$V_{GS}$ = 0.5")
plt.plot(sn2[:,0],sn2[:,1],label=r"$V_{GS}$ = 1")
plt.plot(sn3[:,0],sn3[:,1],label=r"$V_{GS}$ = 1.5")
plt.plot(sn4[:,0],sn4[:,1],label=r"$V_{GS}$ = 2")
plt.plot(c[:,0],c[:,1],label=r"$V_{GS} - V_{Th}$")
plt.title("Short Channel NMOS")
plt.grid()
plt.legend()
plt.xlabel(r"$V_{D}$")
plt.ylabel(r"$I_{D}$")

plt.subplot(2,2,4)
plt.plot(sp1[:,0],sp1[:,1],label=r"$V_{GS}$ = -0.5")
plt.plot(sp2[:,0],sp2[:,1],label=r"$V_{GS}$ = -1")
plt.plot(sp3[:,0],sp3[:,1],label=r"$V_{GS}$ = -1.5")
plt.plot(sp4[:,0],sp4[:,1],label=r"$V_{GS}$ = -2")
plt.plot(d[:,0],d[:,1],label=r"$V_{GS} - V_{Th}$")
plt.title("Short Channel PMOS")
plt.grid()
plt.legend()
plt.xlabel(r"$V_{D}$")
plt.ylabel(r"$I_{D}$")

plt.savefig("4b.png")
plt.show()

