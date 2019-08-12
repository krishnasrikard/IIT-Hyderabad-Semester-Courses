# Generating Signals

import numpy as np
import matplotlib.pyplot as plt

def Sin_Discrete(a,b,F,A = 1,f = 1):									# Function to generate Discrete Sinusoid
	"""
	A = Amplitude
	F = Sampling Frequency
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""	
	time = np.arange(a,b,1)
	amplitude = A*np.sin(2*np.pi*time*f/F)
	
	return amplitude,time
	
x1 = np.zeros(201)
t = np.ones(101)
for i in range(101):
	t[i] = 0.9 ** i

a1,a2 = 2,5

x1[100:] = t
x2,time = Sin_Discrete(-100,101,f=200,F=8000)


plt.figure(figsize=(15, 10))
ax = plt.subplot(1, 2, 1)
plt.stem(time,x1)
ax = plt.subplot(1, 2, 2)
plt.stem(time,x2)
plt.show()



