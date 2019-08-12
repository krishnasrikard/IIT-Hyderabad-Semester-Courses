# We will try to implement add noise to audio file and filter it in this program.

import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write


rate,audio_original = read('Audio_Original.wav')
audio = audio_original[:,0]
write("Audio_Modified.wav",rate,audio)
print (audio.shape[0])
print (audio.shape[0]/rate)												# Time of track
# print (audio.shape[1])												# No.of Channels

write("Audio_with_Noise.wav",rate,audio)								# Creating a .wav file

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
	"""
	p,q,s = M,audio.shape[0]- M,audio.shape[0]
	audio_change = np.zeros(s+2*M)
	audio_change[M:s+M] = audio
	audio_new = np.zeros(s)
		
	for i in range(M,s+M):
		audio_new[i-M] = np.mean(audio_change[i-M:i+M])
	
	time = np.arange(s)	
	
	return audio_new,time
	
def System_Function_Mean_Filter(M = 10):								# h[n] for Mean Filter
	"""
	size = Size of signal that is going to be convolved
	M = Size of Filter
	"""

	time = np.arange(0,2*M+1)
	System_Function = np.ones(2*M + 1)
	
	return System_Function/(2*M + 1)

def Convolution(A,B):													# Function to Convolve 2 signals using numpy
	output = np.convolve(A,B)
	s = output.shape[0]
	time = np.arange(0,s)
	return output,time


audio = Add_Noise(audio)
Plot_Audio(audio)

h = System_Function_Mean_Filter()
audio_conv,time_conv = Convolution(audio,h)
Plot_Audio(audio_conv)
write("Audio_with_Convolution.wav",rate,audio_conv)						# Creating filtered audio signal using Mean Filter and convolution
