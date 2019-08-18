# We will try to reverse,get even and odd parts of given signal

import numpy as np
import matplotlib.pyplot as plt

n = int(input("No.of Elements in signal: "))
x = np.ones(n)
time = np.arange(n)

for i in range(n):														# Generating the input
	x[i] = 0.95 ** i

	
def Reverse_Signal(signal):												# Function to reverse a signal
	"""
	Now we will reverse the given signal.
	"""
	
	reverse_signal = signal[::-1]
	
	return reverse_signal

def Even_Signal_Component(signal):										# Function to get even component of signal
	"""
	Now we get the even component of signal
	"""
	
	even_signal = signal[0::2]
	
	return even_signal
		
def Odd_Signal_Component(signal):										# Function to get odd component of signal
	"""
	Now we get the odd component of signal
	"""
	
	odd_signal = signal[1::2]
	
	return odd_signal
	
x_reverse = Reverse_Signal(x)
s = x_reverse.shape[0]
time_reverse = np.arange(-s+1,1)

x_even_component = Even_Signal_Component(x)
s = x_even_component.shape[0]
time_even_component = np.arange(s)

x_odd_component = Odd_Signal_Component(x)
s = x_odd_component.shape[0]
time_odd_component = np.arange(s)

fig,ax = plt.subplots(2,2)

ax[0,0].stem(time,x,'b')
ax[0,0].set_title('Signal')
ax[0,1].stem(time_reverse,x_reverse,'r')
ax[0,1].set_title('Reversed Signal')
ax[1,0].stem(time_even_component,x_even_component,'g')
ax[1,0].set_title('Signal Even Components')
ax[1,1].stem(time_odd_component,x_odd_component,'y')
ax[1,1].set_title('Signal Odd Components')

plt.show()
