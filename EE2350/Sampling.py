# We will try to implement "Sampling" in this program.

import numpy as np
import matplotlib.pyplot as plt

def Sine(a,b,A = 1,f = 1):
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
	
def Sine_Sampling(a,b,F,A = 1,f = 1):
	"""
	A = Amplitude
	F = Sampling Frequency
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""	
	time = np.arange(a,b,1)
	amplitude = A*np.sin(2*np.pi*time*f/F)
	
	plt.title("Discrete Sine Wave")
	plt.xlabel("Time")
	plt.ylabel("Amplitude")
	plt.stem(time,amplitude)
	plt.show()


Sine(0,20,f = 1/8)
Sine_Sampling(0,20,8)
