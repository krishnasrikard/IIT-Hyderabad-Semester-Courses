# The Following is written to run in Termux

import numpy as np
import matplotlib.pyplot as plt
# Import the below Libraries if running on Termux
import subprocess
import shlex

def h(N):
	"""
	Generate h[n]
	"""
	h = []
	for i in range(N):
		o = 0;
		if i >= 0:
			o += pow(-0.5,i)
		if i-2 >= 0:
			o += pow(-0.5,i-2)
		h.append(o)
		
	return h

def Pad(x):
	"""
	Padding Signal to perform Radix-2 FFT
	"""	
	x = np.asarray(x)
	n = x.shape[0]
	l = pow(2,int(np.ceil(np.log2(n))))
	Padded_x = np.zeros((l,))
	Padded_x[:n] = x
	return Padded_x
	
x = Pad([1,2,3,4,2,1])
N = 250
h = Pad(h(N))

PythonH = np.fft.fft(h)
PythonX = np.fft.fft(x)

CH = np.loadtxt('FFTh.dat',dtype= 'float')
CH = CH[:,0] + 1j * CH[:,1]
CX = np.loadtxt('FFTx.dat',dtype= 'float')
CX = CX[:,0] + 1j * CX[:,1]

# Verification:
print ("Verification of X[n]:", np.all(np.round(CX,3) == np.round(PythonX,3)))
print ("Verification of H[n]:", np.all(np.round(CH,3) == np.round(PythonH,3)))

