# We will try to implement "Quantisation" in this program.

import numpy as np
import matplotlib.pyplot as plt

def Sin_Continous(a,b,A = 1,f = 1):										# Function to generate and plot a Continous Sin
	"""
	A = Amplitude
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""
	time = np.arange(a,b,0.01)
	amplitude = A*np.sin(2*np.pi*f*time)
	
	plt.title("Sine Wave")
	plt.xlabel("Time")
	plt.ylabel("Amplitude")
	plt.plot(time,amplitude)
	plt.show()
	
	return amplitude,time

def Sin_Quantisation(a,b,N,A = 1,f = 1):								# Function to plot quantised Sin wave
	"""
	A = Amplitude
	N = no.of bits
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""
	time = np.arange(a,b,0.01)
	amplitude = A*np.sin(2*np.pi*f*time)
	b,a = max(amplitude),min(amplitude)
	
	amplitude_new = np.ceil((amplitude - a)*(2**N - 1)/(b-a))
	amplitude_new = (amplitude_new /(2**N - 1))*(b-a) + a
	
	plt.title("Quantised Sine Wave")
	plt.xlabel("Time")
	plt.ylabel("Amplitude")
	plt.stem(time,amplitude_new)
	plt.show()
	
	return amplitude_new,time
	
	
Sin_Continous(0,5)
Sin_Quantisation(0,5,4)
