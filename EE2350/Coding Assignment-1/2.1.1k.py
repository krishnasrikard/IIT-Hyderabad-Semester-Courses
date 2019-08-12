# Simulating a Squarer Wave

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
	
def Squarer_System(x):													# Function to apply filter on a array 
	"""
	Applying Backward Differencing System/Filter on an array
	"""
	n = x.shape[0]
	output = np.zeros(n)
	
	for i in range(n):
		output[i] = x[i] * x[i]	

	return output
	
S,time = Sin_Discrete(0,50,32)

S_square = Squarer_System(S)

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.stem(time,S,'r')

ax = plt.subplot(1,2,2)
plt.stem(time,S_square,'y')

plt.show()
