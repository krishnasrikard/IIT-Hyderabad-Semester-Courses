# In this We will try to check wheter Mean_Filter is LTI system or not

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

def Cos_Discrete(a,b,F,A = 1,f = 1):									# Function to generate Discrete Cosine
	"""
	A = Amplitude
	F = Sampling Frequency
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""	
	time = np.arange(a,b,1)
	amplitude = A*np.cos(2*np.pi*time*f/F)
	
	return amplitude,time
		
C,time = Cos_Discrete(0,50,32)
S,time = Sin_Discrete(0,50,32)
Sum = np.add(S,C)

#plt.stem(time,S)
#plt.stem(time,C,'y')
#plt.show()

C_noise = Add_Noise(C)
S_noise = Add_Noise(S)
Sum_noise = S_noise + C_noise

#plt.stem(time,S_noise)
#plt.stem(time,C_noise,'r')
#plt.show()

plt.stem(time,Sum_noise)
plt.show()

C_filtered_Mean,time = Mean_Filter(C_noise,10)
S_filtered_Mean,time = Mean_Filter(S_noise,10)
Filtered_Sum = S_filtered_Mean + C_filtered_Mean

Sum_filtered_Mean,time = Mean_Filter(Sum_noise,10)

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.stem(time,Filtered_Sum,'r')

ax = plt.subplot(1,2,2)
plt.stem(time,Sum_filtered_Mean,'y')

plt.show()
