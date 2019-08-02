# We will try to implement add noise to audio file and filter it in this program.

import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write


rate,audio_original = read('Audio_Original.wav')
audio = audio_original[:,0]
write("Audio_modified.wav",rate,audio)
print (audio.shape[0])
print (audio.shape[0]/rate)								# Time of track
# print (audio.shape[1])								# No.of Channels

write("Audio_with_Noise.wav",rate,audio)

def Plot_Audio(audio):
	s = audio.shape[0]
	time = np.arange(s)
	plt.plot(time,audio)
	plt.show()

def Add_Noise(audio,mu = 0,sigma = 1):
	gaussian_noise = np.random.normal(0, 1, audio.shape[0])
	audio = audio + gaussian_noise
	
	return audio
	
def Median_Filter(audio,M):
	p,q,s = M,audio.shape[0]- M,audio.shape[0]
	audio_change = np.zeros(s+2*M)
	audio_change[M:s+M] = audio
	audio_new = np.zeros(s)
		
	for i in range(M,s+M):
		audio_new[i-M] = np.median(audio_change[i-M:i+M])
	
	time = np.arange(s)	
	
	return audio_new,time

def Mean_Filter(audio,M):
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
write("Audio_with_Noise.wav",rate,audio)
Plot_Audio(audio)

audio_new_mean,time_new = Mean_Filter(audio,2)
Plot_Audio(audio_new_mean)
write("Audio_with_Noise_Filtered_Mean.wav",rate,audio_new_mean)
		
audio_new_median,time_new = Median_Filter(audio,1)
Plot_Audio(audio_new_median)
write("Audio_with_Noise_Filtered_Median.wav",rate,audio_new_median)
