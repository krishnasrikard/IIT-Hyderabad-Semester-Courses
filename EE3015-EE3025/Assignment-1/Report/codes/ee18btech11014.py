import numpy as np
import matplotlib.pyplot as plt

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
	
x = [1,2,3,4,2,1]
N = len(x)
h = h(N)

print ("DFT of x(n)\n",DFT(x))
print()
print ("DFT of h(n)\n",DFT(h))
