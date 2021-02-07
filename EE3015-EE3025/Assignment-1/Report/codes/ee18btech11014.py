# The Following is written to run in Termux

import numpy as np
import matplotlib.pyplot as plt
# Import the below Libraries if running on Termux
import subprocess
import shlex

def h(N):
	h = []
	for i in range(N):
		o = 0;
		if i >= 0:
			o += pow(-0.5,i)
		if i-2 >= 0:
			o += pow(-0.5,i-2)
		h.append(o)
		
	return h

def DFT(s):
	S = []
	N = len(s)
	for k in range(N):
		o = 0 * 1j
		for n in range(N):
			o += s[n] * np.exp(-1j*2*np.pi*k*n/N)
		S.append(o)
	return S

def DFTMatrix(s):
	N = len(s)
	W = 1j * np.zeros((N,N))
	w = np.exp(-1j * 2.0 * np.pi/N)
	for i in range(N):
		for j in range(N):
			W[i][j] = pow(w,i*j)
	
	S = np.dot(W,s)
	return S
	
x = [1,2,3,4,2,1]

N = 200
h = h(N)

X = DFTMatrix(x)
H = DFTMatrix(h)

print ("DFT of x(n)\n",X)
print()
print ("DFT of h(n)\n",H)

plt.figure(figsize=(9,7.5))

plt.subplot(2,2,1)
plt.stem(np.abs(X))
plt.title(r'$|X(k)|$')
plt.grid()

plt.subplot(2,2,2)
plt.stem(np.angle(X))
plt.title(r'$\angle{X(k)}$')
plt.grid()

plt.subplot(2,2,3)
plt.plot(np.abs(H))
plt.title(r'$|H(k)|$')
plt.grid()

plt.subplot(2,2,4)
plt.plot(np.angle(H))
plt.title(r'$\angle{H(k)}$')
plt.grid()

plt.savefig('../figs/Plot.eps')
plt.savefig('../figs/Plot.pdf')

''' If using Termux '''
subprocess.run(shlex.split("termux-open ../figs/Plot.pdf"))

#plt.show()
