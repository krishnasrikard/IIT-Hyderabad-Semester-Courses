# We will try to implement "Sampling" in this program.

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
	
def Sin_Sampling(a,b,F,A = 1,f = 1):									# Function to plot sampled Sin wave
	"""
	A = Amplitude
	F = Sampling Frequency
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""	
	time = np.arange(a,b,1)
	amplitude = A*np.sin(2*np.pi*time*f/F)
	
#	plt.title("Discrete Sine Wave")
#	plt.xlabel("Time")
#	plt.ylabel("Amplitude")
#	plt.stem(time,amplitude)
#	plt.show()
	
	return amplitude,time


frequencies = [1,2,3,3.5,4,5,6,7]

for i in frequencies:
	x,t = Sin_Sampling(0,100,F = 8000,f = i*1000)
	y,t = Sin_Sampling(0,100,F = 80000,f = i*1000)
	
	plt.stem(t,x,'r')
	plt.stem(t,y,'y')
	plt.show()
