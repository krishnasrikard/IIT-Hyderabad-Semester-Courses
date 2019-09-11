import numpy as np
import matplotlib.pyplot as plt

def Sin_Continous(a,b,A = 1,f = 1):										# Function to generate and plot a Continous Sin
	"""
	A = Amplitude
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""
	time = np.arange(a,b,0.01)
	amplitude = A*np.sin(f*time)
	
	return amplitude,time

def function1(L,a,b):													# Generating Harmonics of Sine Wave,adding them and plotting them.
	"""
	L = Limit
	"""
	
	N = np.arange(1,L,1)												
	time = np.arange(a,b,0.01)
	s = time.shape[0]
	output = np.zeros(s)
	
	for n in N:
		output += (Sin_Continous(a,b,A=1/n,f=n))[0]
		
	plt.xlabel("Time")
	plt.ylabel("Output")
	plt.plot(time,output)
	plt.show()
		
	return output,time
	
def function2(L,a,b):													# Generating Odd Harmonics of Sine Wave,adding them and plotting them.
	"""
	L = Limit
	"""
	
	N = np.arange(1,L,2)												
	time = np.arange(a,b,0.01)
	s = time.shape[0]
	output = np.zeros(s)
	
	for n in N:
		output += (Sin_Continous(a,b,A=1/(n),f=n))[0]
		
	plt.xlabel("Time")
	plt.ylabel("Output")
	plt.plot(time,output)
	plt.show()
		
	return output,time
	
function1(100,0,4*np.pi)
function2(100,0,4*np.pi)	