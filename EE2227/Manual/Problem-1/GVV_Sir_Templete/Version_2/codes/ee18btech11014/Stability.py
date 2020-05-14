# License
'''
Code by Krishna Srikar Durbha
May 12,2020
Released under GNU GPL
'''

import numpy as np
import matplotlib.pyplot as plt
import subprocess
from scipy.signal import lti, step2
import shlex

H = 1.11e-3
Gm = 1/H
GmdB = 20*np.log10(Gm)

def FreqG(GmdB):
	'''
	Calculates Frequency from Gain of G(f) in dB
	'''
	if GmdB >= 100:
		f = 1e5
	elif (GmdB < 100 and GmdB >= 80):
		f = 10**((200-GmdB)/20)
	elif (GmdB < 80 and GmdB >= 40):
		f = 10**((320-GmdB)/40)
	else:
		f = 10**((460-GmdB)/60)
		
	return f
	
def PhaseG(f):
	'''
	Calculates Phase of G(f) from f
	'''
	phase = -180*(np.arctan(f/1e5) + np.arctan(f/1e6) + np.arctan(f/1e7))/np.pi
	return phase

def Stability(Phase):
	'''
	Determains Phase Margin and Stability from Phase
	'''
	PhaseMargin = 180.0 + np.round(Phase,decimals=1)
	print ("Phase-Margin =",PhaseMargin)
	
	if PhaseMargin > 0:
		print ("Stable System")
	elif PhaseMargin == 0:
		print ("Marginally Stable System")
	else:
		print ("Unstable System")
		
	return PhaseMargin

if (GmdB <= 100):
	f = FreqG(GmdB)
	Phase = PhaseG(f)
	PhaseMargin = Stability(Phase)
else:
	print ('System is Stable as |GH| is never equal to 1')
