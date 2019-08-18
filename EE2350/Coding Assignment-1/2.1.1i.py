# Code for simulating y[n] = x[n] - 2x[n-1] + x[n-2]

import numpy as np
import matplotlib.pyplot as plt

def Convolution_Manual(A,B):											# Function to Convolve 2 signals without using numpy
	a,b = A.shape[0],B.shape[0]
	s = a+b-1
	output = np.zeros(s)
	time = np.arange(0,s)
	
	for n in range(s):
		for k in range(a):
			j = n - k
			if (j < 0 or j > b-1):
				l = 0
			else:
				l = B[j]
				
			output[n] += A[k] * l	
			
	return output,time
	
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
	
def Filter(S):															# Function generator
	"""
	y[n] = x[n] - 2x[n-1] + x[n-2]
	h[n] = {1, -2, 1}  ------- Can be used if we want to use convolution
	Convolution_Manual can be used to convolve.
	"""
	s = S.shape[0]
	Y = np.zeros(s+2)
	time_output = np.arange(s+2)
										
	for i in range(s+2):
		a,b,c = i,i-1,i-2
	
		if (a < 0 or a > s-1):
			l = 0
		else:
			l = S[i]
		
		if (b < 0 or b > s-1):
			m = 0
		else:
			m = S[i-1]
		
		if (c < 0 or c > s-1):
			n = 0
		else:
			n = S[i-2]
		
		
		Y[i] = l - 2*m + n
		
	return Y,time_output
	


S,time = Sin_Discrete(0,50,32)
Y,time_output = Filter(S)

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.stem(time,S,'r')

ax = plt.subplot(1,2,2)
plt.stem(time_output,Y,'y')

plt.show()
