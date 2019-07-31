# We will try to implement "Moving Medain Filter" in this program.

import numpy as np
import matplotlib.pyplot as plt

def Sine(a,b,A = 1,f = 1):
	"""
	A = Amplitude
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""
	time = np.arange(a,b,0.001)
	amplitude = A*np.sin(2*np.pi*f*time)
	
	plt.title("Sine Wave")
	plt.xlabel("Time")
	plt.ylabel("Amplitude")
	plt.plot(time,amplitude)
	plt.show()

def Sine_Noise(a,b,A = 1,f = 1,sigma = 1,mu = 0):
	"""
	A = Amplitude
	sigma = Standard Deviation of Gaussian Noise
	mu = mean of Gaussian Noise
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""
	time = np.arange(a,b,0.001)
	amplitude = A*np.sin(2*np.pi*f*time)
	
	gaussian_noise = np.random.normal(mu, sigma, np.shape(amplitude))
	amplitude = amplitude + gaussian_noise
		
	plt.title("Sine Wave with Noise")
	plt.xlabel("Time")
	plt.ylabel("Amplitude")
	plt.plot(time,amplitude)
	plt.show()
	
def Median_Filter(a,b,M,A = 1,f = 1,sigma = 1,mu = 0):
	"""
	A = Amplitude
	M = Range of Filter
	sigma = Standard Deviation of Gaussian Noise
	mu = mean of Gaussian Noise
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""
	time = np.arange(a,b,0.001)
	amplitude = A*np.sin(2*np.pi*f*time)
	
	gaussian_noise = np.random.normal(mu, sigma, np.shape(amplitude))
	amplitude = amplitude + gaussian_noise
	
	p,q,s = M,amplitude.shape[0]- M,amplitude.shape[0]- 2*M
	amplitude_new = np.zeros(s)
	time_new = np.zeros(s)
		
	for i in range(p,q):
		amplitude_new[i-p] = np.median(amplitude[i-M:i+M])
		time_new[i-p] = time[i]
		
	plt.title("Sine Wave with Noise Filter after applied")
	plt.xlabel("Time")
	plt.ylabel("Amplitude")
	plt.plot(time_new,amplitude_new)
	plt.show()

Sine(0,5)
Sine_Noise(0,5)
Median_Filter(0,5,100)
