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
	
	k = np.arange(1,L,2)
	s = k.shape[0]
	N = np.zeros(2*s)
	N[0:s]= -k[::-1]
	N[s:2*s]= k
	i = 0
	
	u = N.shape[0]
	spectrum = np.zeros(u)
	phase = np.zeros(u)
		
	for n in N:
		spectrum[i] = abs(1/(2*np.pi*n))
		phase[i] = (n/abs(n))*(np.pi)*0.5
		
		i = i+1
	
	plt.figure(figsize=(13, 8))
	ax = plt.subplot(1,2,1)
	plt.plot(N,phase)
	
	ax = plt.subplot(1,2,2)
	plt.plot(N,spectrum)
	plt.show()

	return N,spectrum

def Triangle_Wave(a,b,L=1500):											# Generating Triangle Wave Fourier Spectrum
	"""
	L = Limit
	"""
	
	k = np.arange(1,L,2)
	s = k.shape[0]
	N = np.zeros(2*s)
	N[0:s]= -k[::-1]
	N[s:2*s]= k
	i = 0
	
	u = N.shape[0]
	spectrum = np.zeros(u)
	phase = np.zeros(u)
		
	for n in N:
		spectrum[i] = abs(1/(2*np.pi*n**2))
		phase[i] = (n**2/abs(n**2))*(np.pi)*0.5
		
		i = i+1
	
	plt.figure(figsize=(13, 8))
	ax = plt.subplot(1,2,1)
	plt.plot(N,phase)
	
	ax = plt.subplot(1,2,2)
	plt.plot(N,spectrum)
	plt.show()

	return N,spectrum

Square_Wave(-2,2,L=15)
Triangle_Wave(-2,2,L=15)
