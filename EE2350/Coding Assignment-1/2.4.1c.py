# We will try to implement add noise to audio file and filter it using Mean Filter and Fing Signal to Noise Ratio.

import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy import stats


rate,audio_original = read('Audio.wav')
audio = audio_original[:,0]
#write("Audio_Modified.wav",rate,audio)
print (audio.shape[0])
print (audio.shape[0]/rate)												# Time of track
# print (audio.shape[1])												# No.of Channels

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

Plot_Audio(audio)
audio = Add_Noise(audio)
Plot_Audio(audio)
# write("Audio_with_Noise.wav",rate,audio)								# Creating a Audio signal with noise

audio_new_mean,time_new = Mean_Filter(audio,2)
Plot_Audio(audio_new_mean)
# write("Audio_with_Noise_Filtered_Mean.wav",rate,audio_new_mean)		# Creating filtered audio signal using Mean Filter

print (stats.signaltonoise(audio, axis = 0, ddof = 0))					# Signal to Noise Ratio for Noisy signal
print (stats.signaltonoise(audio_new_mean, axis = 0, ddof = 0))			# Signal to Noise Ratio for Enhanced signal
