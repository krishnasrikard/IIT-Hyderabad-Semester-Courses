# We will try to implement "Quantisation" in this program.

import numpy as np
import matplotlib.pyplot as plt

def Sin_Continous(a,b,A = 1,f = 1):
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

def Sin_Quantisation(a,b,N,A = 1,f = 1):
	"""
	A = Amplitude
	N = no.of bits
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""
	time = np.arange(a,b,0.1)
	amplitude = A*np.sin(2*np.pi*f*time)
	D = max(amplitude) - min(amplitude)
	mean = np.mean(amplitude)
	amplitude = np.ceil((amplitude - mean)*(2**N - 1)/D)
	
	plt.title("Quantised Sine Wave")
	plt.xlabel("Time")
	plt.ylabel("Amplitude")
	plt.stem(time,amplitude)
	plt.show()

Sin_Continous(0,5)
Sin_Quantisation(0,5,4)
