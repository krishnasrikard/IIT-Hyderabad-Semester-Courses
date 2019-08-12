# Code for Simulating Backward Propagation System

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
	
		
S,time = Sin_Discrete(0,50,32)

def Backward_Differencing_System(S):									# Function of Backward Differencing System
	"""
	y[n] = x[n] - x[n-1]
	"""
	s = S.shape[0]
	Y = np.zeros(s+1)
	time_output = np.arange(s+1)
	
	for i in range(s+1):
		a,b = i,i-1
		
		if (a < 0 or a > s-1):
			l = 0
		else:
			l = S[i]
		
		if (b < 0 or b > s-1):
			m = 0
		else:
			m = S[i-1]
		
		Y[i] = l - m

	
	return Y,time_output


S,time = Sin_Discrete(0,50,32)
Y,time_output = Backward_Differencing_System(S)

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.stem(time,S,'r')
ax = plt.subplot(1,2,2)
plt.stem(time_output,Y,'y')

plt.show()
