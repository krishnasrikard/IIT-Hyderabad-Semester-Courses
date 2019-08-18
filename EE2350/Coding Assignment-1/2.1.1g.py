# Code for Moving Average System

import numpy as np
import matplotlib.pyplot as plt

n = int(input("No.of Elements in signal: "))
x = np.ones(n)
time = np.arange(n)

for i in range(n):														# Generating the input
	x[i] = 0.95 ** i
	
def Signal_Ideal_Delay(signal,d = 2):									# Function to generate ideal delay in signal
	"""
	Now we get ideal delay in signal
	"""
	s = signal.shape[0]
	time = np.arange(+d,s+d)
	
	return signal,time

def Moving_Average_System(signal,M = 10):								# Function of Moving Average System using Ideal Delay System							
	"""
	Moving Average System using Ideal Delay System.
	"""
	p,q,s = M,signal.shape[0]- M,signal.shape[0]
	signal_new = np.zeros(s+M)
	
	for i in range(M+1):
		signal_new[M-i:M-i+s] += Signal_Ideal_Delay(signal,d=i)[0]
		
	signal_new = signal_new/(M + 1)		
	time = np.arange(0,s+M)
	
	return signal_new,time
	
	
x_filtered,time_filtered = Moving_Average_System(x)

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.stem(time,x,'r')

ax = plt.subplot(1,2,2)
plt.stem(time_filtered,x_filtered,'y')

plt.show()
