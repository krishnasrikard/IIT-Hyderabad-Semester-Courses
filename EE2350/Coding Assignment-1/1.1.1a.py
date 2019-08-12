# We will try to decimate the audio signal and save it with different sampling rate

import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write
import scipy.signal

rate,audio_original = read('audio.wav')									# Reading a music file
audio = audio_original[:,0]												# Considering the stereo channel to solve

print (audio.shape[0])
print (audio.shape[0]/rate)												# Time of track
print (rate)															# Sample Rate


dsr = [2,4,8,16,32]														# Decimating Factors

for i in dsr:
	audio_new = scipy.signal.decimate(audio,i)							# Decimating the audio signal						
	fs = int(rate/i)													# Sampling Frequency
	a = "audio_dsr="+str(i)+".wav"										# Name of "audio" file
	write(a,fs,audio)													# Saving the audio file
	
