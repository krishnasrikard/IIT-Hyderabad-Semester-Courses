import numpy as np
import matplotlib.pyplot as plt

def Cos_Continous(a,b,A = 1,f = 1):										# Function to generate and plot a Continous Cos
	"""
	A = Amplitude
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""
	time = np.arange(a,b,0.01)
	amplitude = A*np.cos(f*time)
	
	return amplitude,time

def function(L,a,b):													# Generating Odd Harmonics of Cos Wave,adding them and plotting them.
	"""
	L = Limit
	"""
	
	N = np.arange(1,L,2)												
	time = np.arange(a,b,0.01)
	s = time.shape[0]
	output = np.zeros(s)
	
	for n in N:
		output += (Cos_Continous(a,b,A=1/(n**2),f=n))[0]
		
	plt.xlabel("Time")
	plt.ylabel("Output")
	plt.plot(time,output)
	plt.show()
		
	return output,time
	
function(50,0,4*np.pi)	
