# Code for simulating y[n] = x[n-2] + x[2-n]

import numpy as np
import matplotlib.pyplot as plt

def Sin_Discrete(a,b,F,A = 1,f = 1):									# Function to generate Discrete Sinusoid
	"""
	A = Amplitude
	F = Sampling Frequency
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""	
	time = np.arange(a,b,1)
	amplitude = A*np.sin(2*np.pi*time*f/F)
	
	return amplitude,time

def Filter(S):															# Function for Generating Filter
	"""
	y[n] = x[2-n] + x[n-2]
	"""
	n = S.shape[0]
	Y = np.zeros(n)
	time_output = np.arange(n)

	for i in range(n):
		a,b = i - 2,2 - i
	
		if (a < 0):
			l = 0
		else:
			l = S[a]
		
		if (b < 0):
			m = 0
		else:
			m = S[b]
		
	
		Y[i] = l + m
		
	return Y,time_output
	
	
S,time = Sin_Discrete(0,50,32)
Y,time_output = Filter(S)
	
plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.stem(time,S,'r')
ax = plt.subplot(1,2,2)
plt.stem(time_output,Y,'y')

plt.show()
