import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write
import scipy.signal

rate,audio_original = read('audio.wav')
audio = audio_original[:,0]

print (audio.shape[0])
print (audio.shape[0]/rate)												# Time of track
print (rate)

def Audio_Quantisation(audio,N = 4):									# Function to plot quantised audio wave
	"""
	audio = Audio signal
	N = bits per sample
	"""
	
	b,a,D = max(audio),min(audio),max(audio) - min(audio)
	s = audio.shape[0]
	time = np.arange(s)
	
	mean = np.mean(audio)
	audio_new = np.ceil((audio - mean)*(2**N - 1)/(b-a))
	audio_new = (audio_new /(2**N - 1))*(b-a) + mean
	
#	plt.title("Quantised Audio Wave")
#	plt.xlabel("Time")
#	plt.ylabel("audio")
#	plt.stem(time,audio_new)
#	plt.show()
	
	return audio_new

N = [3,2,1]
for i in N:
	audio_quantised = Audio_Quantisation(audio)
	audio_difference = audio - audio_quantised
	a = "audio_quantised_bits="+str(i)+".wav"
	b = "audio_difference_bits="+str(i)+".wav"
	write(a,rate,audio_quantised)										# Saving the audio file
	write(b,rate,audio_difference)										# Saving the audio file
