# We will try to implement add noise to audio file and filter it in this program.

import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write


rate,audio = read('Audio.wav')

print (audio)
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
	
def Mean_Filter(audio,M):
	p,q,s = M,audio.shape[0]- M,audio.shape[0]- 2*M
	audio_new = np.zeros(s)
		
	for i in range(p,q):
		audio_new[i-p] = np.mean(audio[i-M:i+M])
	
	time = np.arange(s)	
	plt.plot(time,audio_new)
	plt.show()

		
	return audio_new

def Median_Filter(audio,M):
	p,q,s = M,audio.shape[0]- M,audio.shape[0]- 2*M
	audio_new = np.zeros(s)
		
	for i in range(p,q):
		audio_new[i-p] = np.median(audio[i-M:i+M])
	
	time = np.arange(s)
	plt.plot(time,audio_new)
	plt.show()
	
	return audio_new


Plot_Audio(audio)
audio = Add_Noise(audio)
write("Audio_with_Noise.wav",rate,audio)
Plot_Audio(audio)

audio_new_mean = Mean_Filter(audio,100)
write("Audio_with_Noise_Filtered_Mean.wav",rate,audio_new_mean)
		
audio_new_median = Median_Filter(audio,100)
write("Audio_with_Noise_Filtered_Median.wav",rate,audio_new_median)
