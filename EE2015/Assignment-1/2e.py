import numpy as np
import matplotlib.pyplot as plt
import math

def Sin_Continous(a,b,A = 1,f = 1):										# Function to generate and plot a Continous Sin
	"""
	A = Amplitude
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""
	time = np.arange(a,b,0.01)
	amplitude = A*np.sin(2*np.pi*f*time)
	
	return amplitude,time
	
def Cos_Continous(a,b,A = 1,f = 1):										# Function to generate and plot a Continous Cos
	"""
	A = Amplitude
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""
	time = np.arange(a,b,0.01)
	amplitude = A*np.cos(2*np.pi*f*time)
	
	return amplitude,time

def Square_Wave(a,b,L=1500):											# Generating Square Wave Fourier Spectrum
	"""
	L = Limit
	"""
	
	N = np.arange(1,L,2)
	u = N.shape[0]
	spectrum = np.zeros(u)
		
	for n in N:
		spectrum[int(n/2)] = 1/n
		
	plt.plot(N,spectrum)
	plt.show()

	return N,spectrum

def Triangle_Wave(a,b,L=1500):											# Generating Triangle Wave Fourier Spectrum
	"""
	L = Limit
	"""
	
	N = np.arange(1,L,2)
	u = N.shape[0]
	spectrum = np.zeros(u)
	
	for n in N:
		spectrum[int(n/2)] = 1/n**2
	
	plt.plot(N,spectrum)
	
	plt.show()
		
	return N,spectrum

Square_Wave(-2,2,L=15)
Triangle_Wave(-2,2,L=15)
