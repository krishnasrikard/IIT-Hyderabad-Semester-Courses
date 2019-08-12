# We will try to decimate the speech signal and save it with different sampling rate

import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write
import scipy.signal

rate,speech_original = read('speech.wav')								# Reading a music file
speech = speech_original[:,0]											# Considering the stereo channel to solve

print (speech.shape[0])
print (speech.shape[0]/rate)											# Time of track
print (rate)															# Sample Rate


dsr = [2,4,8,16,32]														# Decimating Factors

for i in dsr:
	speech_new = scipy.signal.decimate(speech,i)						# Decimating the speech signal						
	fs = int(rate/i)													# Sampling Frequency
	a = "speech_dsr="+str(i)+".wav"										# Name of "speech" file
	write(a,fs,speech)													# Saving the speech file
	
