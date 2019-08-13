# We will try to implement Reverberatation to audio signal.

import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write
import random

rate,audio_original = read('Audio.wav')
audio = audio_original[:,0]
print (audio.shape[0])
print (audio.shape[0]/rate)												# Time of track
# print (audio.shape[1])												# No.of Channels


def Plot_Audio(audio):													# Function to plot Audio Signal
	s = audio.shape[0]
	time = np.arange(s)
	plt.plot(time,audio)
	plt.show()
	
def Attenuation_Coeff1(M = 100):										# Function to calculate Attenuation Coefficient
	"""
	M = No.of Reflections
	"""
	
	h = 0.25 * np.random.rand(1000)
		
	return h
	
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
	
def Reverberation(audio,M=100):											# Function to generate a Reverberated Audio signal
	"""
	M = No.of Refelections
	audio = signal to be Reverberated
	"""
	h = Attenuation_Coeff1(M)
	print (h)
	output = np.convolve(audio,h)
	s = output.shape[0]
	time = np.arange(s)
	
	output,time = Convolution_Manual(audio,h)
	
	return output,time

Plot_Audio(audio)
	
audio_reverb,time = Reverberation(audio)
Plot_Audio(audio_reverb)
write("Audio_Reverberated_new.wav",rate,audio_reverb)					# Creating file for reverberated audio signal
