# We will try to code for Ideal Delay System

import numpy as np
import matplotlib.pyplot as plt

n = int(input("No.of Elements in signal: "))
d = int(input("Enter value of d = "))
x = np.random.rand(n)
time = np.arange(n)

def Signal_Ideal_Delay(signal,d = 2):										# Function to generate ideal delay in signal
	"""
	Now we get ideal delay in signal
	"""
	s = signal.shape[0]
	time = np.arange(+d,s+d)
	
	return signal,time

x_ideal_delay,time_delay = Signal_Ideal_Delay(x,d)

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.stem(time,x,'g')

ax = plt.subplot(1,2,2)
plt.stem(time_delay,x_ideal_delay,'y')

plt.show()
