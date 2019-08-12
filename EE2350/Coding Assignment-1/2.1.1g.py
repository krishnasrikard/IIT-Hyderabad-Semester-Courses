# Code for Moving Average System

import numpy as np
import matplotlib.pyplot as plt

n = int(input("No.of Elements in signal: "))
x = np.ones(n)
time = np.arange(n)

for i in range(n):														# Generating the input
	x[i] = 0.95 ** i
	
def Signal_Ideal_Delay(signal,d):										# Function to generate ideal delay in signal
	"""
	Now we get ideal delay in signal
	"""
	s = signal.shape[0] - d
	signal_delay = signal[d:]
	
	return signal_delay

def Moving_Average_System(signal,M = 10):								# Function of Moving Average System using Ideal Delay System							
	"""
	Moving Average System using Ideal Dealy System.
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
	
	
x_filtered,time = Moving_Average_System(x)

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.stem(time,x,'r')

ax = plt.subplot(1,2,2)
plt.stem(time,x_filtered,'y')

plt.show()
