# We will try to obtain even parts of the input signal

import numpy as np
import matplotlib.pyplot as plt

n = int(input("No.of Elements in signal: "))							
x = np.random.rand(n)													# Generating random numbers as input
time = np.arange(n)

def Even_Signal_Component(signal):										# Function to get even component of signal
	"""
	Now we get the even component of signal
	"""
	
	even_signal = signal[0::2]
	
	return even_signal

x_even_component = Even_Signal_Component(x)
s = x_even_component.shape[0]
time_even_component = np.arange(s)

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.stem(time,x,'g')

ax = plt.subplot(1,2,2)
plt.stem(time_even_component,x_even_component,'y')

plt.show()
