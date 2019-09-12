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

def Square_Wave(a,b,L=1500):											# Generating Square Wave
	"""
	L = Limit
	"""
	
	N = np.arange(1,L,2)
	u = N.shape[0]												
	time = np.arange(a,b,0.01)
	s = time.shape[0]
	output = np.zeros(s)
	spectrum = np.zeros(u)
		
	
	for n in N:
		output += (Sin_Continous(a,b,A=1/(n),f=n))[0]
		spectrum[int(n/2)] = 1/n
	
	output = (output - min(output))/(max(output) - min(output))
	
	plt.figure(figsize=(13, 8))
	ax = plt.subplot(1,2,1)
	plt.plot(time,output)
	
	ax = plt.subplot(1,2,2)
	plt.plot(N,spectrum)
	
	plt.show()

	return output,time

def Triangle_Wave(a,b,L=1500):											# Generating Triangle Wave
	"""
	L = Limit
	"""
	
	N = np.arange(1,L,2)
	u = N.shape[0]													
	time = np.arange(a,b,0.01)
	s = time.shape[0]
	output = np.zeros(s)
	spectrum = np.zeros(u)
	
	for n in N:
		output += (Cos_Continous(a,b,A=1/(n**2),f=n))[0]
		spectrum[int(n/2)] = 1/n**2
	
	output = (output - min(output))/(max(output) - min(output))
			
	plt.figure(figsize=(13, 8))
	ax = plt.subplot(1,2,1)
	plt.plot(time,output)
	
	ax = plt.subplot(1,2,2)
	plt.plot(N,spectrum)
	
	plt.show()
		
	return output,time

Square_Wave(-2,2,L=15)
Triangle_Wave(-2,2,L=15)
