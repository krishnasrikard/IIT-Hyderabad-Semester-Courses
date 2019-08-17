# Code for Moving Average System using Ideal Delay System

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

def Signal_Ideal_Delay(signal,d):										# Function to generate ideal delay in signal
	"""
	Now we get ideal delay in signal
	"""
	s = signal.shape[0] - d
	signal_delay = signal[d:]
	
	return signal_delay

def Moving_Average_System(signal,M = 10):								# Function of Moving Average System using Ideal Delay System							
	"""
	Moving Average System using Ideal Delay System.
	"""
	p,q,s = M,signal.shape[0]- M,signal.shape[0]
	signal_new = np.zeros(s)
	add = np.zeros(s)
		
	for k in range(M+1):
		add[0:s-k] = Signal_Ideal_Delay(signal,k)
		signal_new += add
		
	signal_new = (signal_new)/(M + 1)
	
	time = np.arange(s)	
	
	return signal_new,time
	

S,time = Sin_Discrete(0,50,32)
S_filtered,time = Moving_Average_System(S)

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.stem(time,S,'r')

ax = plt.subplot(1,2,2)
plt.stem(time,S_filtered,'y')

plt.show()
