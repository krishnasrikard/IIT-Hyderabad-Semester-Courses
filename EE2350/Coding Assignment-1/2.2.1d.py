# Understanding Convolution

import numpy as np
import matplotlib.pyplot as plt

def Convolution_Manual(A,B):											# Function to Convolve 2 signals without using numpy
	a,b = A.shape[0],B.shape[0]
	s = a+b-1
	output = np.zeros(s)
	time = np.arange(0,s)
	
	for n in range(s):
		for k in range(a):
			j = n - k
			if (j < 0 or j > b-1):
				l = 0
			else:
				l = B[j]
				
			output[n] += A[k] * l	
			
	return output,time
	
def System_Function_Mean_Filter(M = 10):								# h[n] for Mean Filter
	"""
	size = Size of signal that is going to be convolved
	M = Size of Filter
	"""

	time = np.arange(0,2*M+1)
	System_Function = np.ones(2*M + 1)
	
	return System_Function/(2*M + 1)
	
def Backward_Differencing():											# Back Differencing Filter
	h = np.zeros(2)
	h[0],h[1] = 1.0,-1.0
	
	return h
	
def Apply_Backward_Filter_Array(x):										# Function to apply filter on a array 
	"""
	Applying Backward Differencing System/Filter on an array
	"""
	h = Backward_Differencing()
	s = np.shape(x)
	output,time = Convolution_Manual(x,h)

	return output,time
	
def Filter1():
	h = np.zeros(3)
	h[0],h[1],h[2] = 1.0,-2.0,1.0
	
	return h
	
def Apply_Filter_Array(x):												# Function to apply filter on a array 
	"""
	Applying Backward Differencing System/Filter on an array
	"""
	h = Filter1()
	s = np.shape(x)
	output,time = Convolution_Manual(x,h)

	return output,time
		
		
n = int(input("No.of Elements in signal: "))
x = np.random.rand(n)
time = np.arange(n)

h_mean = System_Function_Mean_Filter()
x_mean,t_mean = Convolution_Manual(x,h_mean)

x_back,t_back = Apply_Backward_Filter_Array(x)
x_filter1,t_filter1 = Apply_Filter_Array(x)

fig,ax = plt.subplots(2,2)

ax[0,0].stem(time,x,'b')
ax[0,0].set_title('Signal')
ax[0,1].stem(t_mean,x_mean,'r')
ax[0,1].set_title('Mean Filtered Signal')
ax[1,0].stem(t_back,x_back,'g')
ax[1,0].set_title('Back Filtered Signal')
ax[1,1].stem(t_filter1,x_filter1,'y')
ax[1,1].set_title('Signal Filtered Filter-1')

plt.show()
