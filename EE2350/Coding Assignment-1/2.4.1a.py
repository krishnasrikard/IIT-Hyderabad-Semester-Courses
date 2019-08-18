# We will try to implement add noise to audio file and filter it using Mean Filter.

import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write


rate,audio_original = read('Audio.wav')
audio = audio_original[:,0]
#write("Audio_Modified.wav",rate,audio)
print (audio.shape[0])
print (audio.shape[0]/rate)												# Time of track
# print (audio.shape[1])												# No.of Channels

def Convolution_Manual(A,B):											# Function to Convolve 2 signals without using numpy
	a,b = A.shape[0],B.shape[0]
	s = a+b-1
	output = np.zeros(s)
	time = np.arange(0,s)
	
	for n in range(s):
		for k in range(a):
			j = n - k
			if (j < 0 or j > b-1):
				l = 0
			else:
				l = B[j]
				
			output[n] += A[k] * l	
			
	return output,time
	
def Plot_Audio(audio):													# Function to plot Audio Signal
	s = audio.shape[0]
	time = np.arange(s)
	plt.plot(time,audio)
	plt.show()

def Add_Noise(audio,mu = 0,sigma = 1):									# Function to add Noise
	"""
	Adding Gaussian Noise
	"""
	gaussian_noise = np.random.normal(0, 1, audio.shape[0])
	audio = audio + gaussian_noise
	
	return audio
	
def Mean_Filter(audio,M):												# Function to apply Mean Filter to audio signal
	"""
	audio = signal on which filter needs to be applied
	M = Bandwidth of filter
	h[n] = np.ones(2*M) --- Can be used if we want to do Convolution
	Convolution can be done by using Convolution_Manual Function.
	"""
	p,q,s = M,audio.shape[0]- M,audio.shape[0]
	audio_change = np.zeros(s+2*M)
	audio_change[M:s+M] = audio
	audio_new = np.zeros(s)
		
	for i in range(M,s+M):
		audio_new[i-M] = np.mean(audio_change[i-M:i+M])
	
	time = np.arange(s)	
	
	return audio_new,time

Plot_Audio(audio)
audio = Add_Noise(audio)
Plot_Audio(audio)
write("Audio_with_Noise.wav",rate,audio)								# Creating a Audio signal with noise

audio_new_mean,time_new = Mean_Filter(audio,2)
Plot_Audio(audio_new_mean)
write("Audio_with_Noise_Filtered_Mean.wav",rate,audio_new_mean)			# Creating filtered audio signal using Mean Filter
