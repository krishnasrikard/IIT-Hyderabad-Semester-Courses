# We will reverse the input signal

import numpy as np
import matplotlib.pyplot as plt

n = int(input("No.of Elements in signal: "))							
x = np.random.rand(n)													# Generating random numbers as input
time = np.arange(n)

def Reverse_Signal(signal):												# Function to reverse a signal
	"""
	Now we will reverse the given signal.
	"""
	
	reverse_signal = signal[::-1]
	
	return reverse_signal

x_reverse = Reverse_Signal(x)
s = x_reverse.shape[0]
time_reverse = np.arange(s)

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.stem(time,x,'g')

ax = plt.subplot(1,2,2)
plt.stem(time_reverse,x_reverse,'y')

plt.show()
