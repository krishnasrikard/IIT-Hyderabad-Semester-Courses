# In this We will use Mean_Filter for filterign a noisy signal

import numpy as np
import matplotlib.pyplot as plt

def Add_Noise(signal,mu = 0,sigma = 1):									# Function to add noise
	gaussian_noise = np.random.normal(0, 1, signal.shape[0])
	signal_noise = signal + gaussian_noise
	
	return signal_noise
	

def Mean_Filter(signal,M):												# Function to apply Mean Filter
	p,q,s = M,signal.shape[0]- M,signal.shape[0]
	signal_change = np.zeros(s+2*M)
	signal_change[M:s+M] = signal
	signal_new = np.zeros(s)
		
	for i in range(M,s+M):
		signal_new[i-M] = np.mean(signal_change[i-M:i+M])
	
	time = np.arange(s)	
	
	return signal_new,time
	
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

def System_Function_Mean_Filter(M = 10):								# h[n] for Mean Filter
	"""
	size = Size of signal that is going to be convolved
	M = Size of Filter
	"""

	time = np.arange(0,2*M+1)
	System_Function = np.ones(2*M + 1)
	
	return System_Function/(2*M + 1)


def Padding_Signal(signal,M = 10):										# Function to pad a signal
	"""
	signal = signal to get paded
	M = no.of elements to be added during padding
	"""
	s = signal.shape[0]
	signal_change = np.zeros(s+2*M)
	signal_change[M:s+M] = signal
	
	return signal_change

def Convolution(A,B):													# Function to Convolve 2 signals using numpy
	output = np.convolve(A,B)
	s = output.shape[0]
	time = np.arange(0,s)
	return output,time
	
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
	

S,time = Sin_Discrete(0,50,32)
S_noise = Add_Noise(S)
S_filtered_Mean,time = Mean_Filter(S_noise,10)

h = System_Function_Mean_Filter()
S_convolution,time_conv = Convolution(S_noise,h)

S_convolution_manual,time_conv_manual = Convolution_Manual(S_noise,h)


plt.figure(figsize=(15, 15))

ax = plt.subplot(1, 3, 1)
plt.stem(time,S_filtered_Mean,'r')

ax = plt.subplot(1,3,2)
plt.stem(time_conv,S_convolution,'g')

ax = plt.subplot(1,3,3)
plt.stem(time_conv_manual,S_convolution_manual,'b')

plt.show()
