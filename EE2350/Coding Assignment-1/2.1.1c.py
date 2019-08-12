# We will try to obtain odd parts of the input signal

import numpy as np
import matplotlib.pyplot as plt

n = int(input("No.of Elements in signal: "))							
x = np.random.rand(n)													# Generating random numbers as input
time = np.arange(n)

def Odd_Signal_Component(signal):										# Function to get odd component of signal
	"""
	Now we get the odd component of signal
	"""
	
	odd_signal = signal[1::2]
	
	return odd_signal

x_odd_component = Odd_Signal_Component(x)
s = x_odd_component.shape[0]
time_odd_component = np.arange(s)

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.stem(time,x,'g')

ax = plt.subplot(1,2,2)
plt.stem(time_odd_component,x_odd_component,'y')

plt.show()
