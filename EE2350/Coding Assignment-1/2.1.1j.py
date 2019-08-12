# code for simulating y1[n] = x[n] - 2x[n-1] + x[n-2] and y2[n] = x[n] - x[n-1]

import numpy as np
import matplotlib.pyplot as plt

s = int(input("No.of Elements in signal: "))							# Generating the input
x = np.ones(s)
time = np.arange(s)

for i in range(s):
	x[i] = 0.95 ** i

	
def Filter(S):															# Function generator
	"""
	y[n] = x[n] - 2x[n-1] + x[n-2]
	"""
	s = S.shape[0]
	Y = np.zeros(s+2)
	time_output = np.arange(s+2)
										
	for i in range(s+2):
		a,b,c = i,i-1,i-2
	
		if (a < 0 or a > s-1):
			l = 0
		else:
			l = S[i]
		
		if (b < 0 or b > s-1):
			m = 0
		else:
			m = S[i-1]
		
		if (c < 0 or c > s-1):
			n = 0
		else:
			n = S[i-2]
		
		
		Y[i] = l - 2*m + n
		
	return Y,time_output
	
	

def Backward_Differencing_System(S):									# Function of Backward Differencing System
	"""
	y[n] = x[n] - x[n-1]
	"""
	s = S.shape[0]
	Y = np.zeros(s+1)
	time_output = np.arange(s+1)
	
	for i in range(s+1):
		a,b = i,i-1
		
		if (a < 0 or a > s-1):
			l = 0
		else:
			l = S[i]
		
		if (b < 0 or b > s-1):
			m = 0
		else:
			m = S[i-1]
		
		Y[i] = l - m

	return Y,time_output


y1,t1 = Backward_Differencing_System(x)
y2,t2 = Filter(x) 


plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 3, 1)
plt.stem(time,x,'r')
ax = plt.subplot(1,3,2)
plt.stem(t1,y1,'y')
ax = plt.subplot(1,3,3)
plt.stem(t2,y2,'y')

plt.show()
