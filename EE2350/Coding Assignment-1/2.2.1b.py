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

def Reverse_Signal(signal):												# Function to reverse a signal
	"""
	Now we will reverse the given signal.
	"""
	
	reverse_signal = signal[::-1]
	
	return reverse_signal

def Even_Signal_Component(signal):										# Function to get even component of signal
	"""
	Now we get the even component of signal
	"""
	
	even_signal = signal[0::2]
	
	return even_signal
	
def Odd_Signal_Component(signal):										# Function to get odd component of signal
	"""
	Now we get the odd component of signal
	"""
	
	odd_signal = signal[1::2]
	
	return odd_signal
	
def Signal_Ideal_Delay(signal,d = 2):									# Function to generate ideal delay in signal
	"""
	Now we get ideal delay in signal
	"""
	s = signal.shape[0]
	time = np.arange(+d,s+d)
	
	return signal,time

def Moving_Average_System(signal,M = 10):								# Function of Moving Average System using Ideal Delay System							
	"""
	Moving Average System using Ideal Delay System.
	"""
	p,q,s = M,signal.shape[0]- M,signal.shape[0]
	signal_new = np.zeros(s+M)
	
	for i in range(M+1):
		signal_new[M-i:M-i+s] += Signal_Ideal_Delay(signal,d=i)[0]
		
	signal_new = signal_new/(M + 1)		
	time = np.arange(0,s+M)
	
	return signal_new,time

def Backward_Differencing_System(S):									# Function of Backward Differencing System
	"""
	y[n] = x[n] - x[n-1]
	h[n] = {1, -1}  ------- Can be used if we want to use convolution
	Convolution_Manual can be used to convolve.
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
	
def Filter_1(S):														# Function generator
	"""
	y[n] = x[n] - 2x[n-1] + x[n-2]
	h[n] = {1, -2, 1}  ------- Can be used if we want to use convolution
	Convolution_Manual can be used to convolve.
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

def Squarer_System(x):													# Function to apply filter on a array 
	"""
	Applying Squarer System/Filter on an array
	"""
	n = x.shape[0]
	output = np.zeros(n)
	
	for i in range(n):
		output[i] = x[i] * x[i]	

	return output
	
def Filter_2(S):														# Function for Generating Filter
	"""
	y[n] = x[2-n] + x[n-2]
	"""
	n = S.shape[0]
	Y = np.zeros(n)
	time_output = np.arange(n)

	for i in range(n):
		a,b = i - 2,2 - i
	
		if (a < 0):
			l = 0
		else:
			l = S[a]
		
		if (b < 0):
			m = 0
		else:
			m = S[b]
		
	
		Y[i] = l + m
		
	return Y,time_output	


a1,a2 = 2,5
x1 = np.zeros(201)
t = np.ones(101)
for i in range(101):
	t[i] = 0.9 ** i
x1[100:] = t
x2,time = Sin_Discrete(-100,101,f=200,F=8000)
Input_Sum = a1*x1 + a2*x2


print ("-------------------------------------------------------------------------------")

y1,y2,Output_Sum = Reverse_Signal(x1),Reverse_Signal(x2),Reverse_Signal(Input_Sum)
Y = a1*y1 + a2*y2

if (np.sum(Y - Output_Sum) == 0):
	print ("Reverse_Signal is Linear System")
else:
	print ("Reverse_Signal is Non-Linear System")
"""
plt.figure(figsize=(13, 8))
ax = plt.subplot(1, 2, 1)
plt.stem(time,Y,'r')
ax = plt.subplot(1,2,2)
plt.stem(time,Output_Sum,'y')
plt.show()
"""
print ("-------------------------------------------------------------------------------")

y1,y2,Output_Sum = Even_Signal_Component(x1),Even_Signal_Component(x2),Even_Signal_Component(Input_Sum)
Y = a1*y1 + a2*y2
y = Y.shape[0]
time = np.arange(y)
if (np.sum(Y - Output_Sum) == 0):
	print ("Even_Signal_Component is Linear System")
else:
	print ("Even_Signal_Component is Non-Linear System")
"""
plt.figure(figsize=(13, 8))
ax = plt.subplot(1, 2, 1)
plt.stem(time,Y,'r')
ax = plt.subplot(1,2,2)
plt.stem(time,Output_Sum,'y')
plt.show()
"""
print ("-------------------------------------------------------------------------------")

y1,y2,Output_Sum = Odd_Signal_Component(x1),Odd_Signal_Component(x2),Odd_Signal_Component(Input_Sum)
Y = a1*y1 + a2*y2
y = Y.shape[0]
time = np.arange(y)
if (np.sum(Y - Output_Sum) == 0):
	print ("Odd_Signal_Component is Linear System")
else:
	print ("Odd_Signal_Component is Non-Linear System")
"""
plt.figure(figsize=(13, 8))
ax = plt.subplot(1, 2, 1)
plt.stem(time,Y,'r')
ax = plt.subplot(1,2,2)
plt.stem(time,Output_Sum,'y')
plt.show()
"""
print ("-------------------------------------------------------------------------------")

y1,t1 = Signal_Ideal_Delay(x1)
y2,t2 = Signal_Ideal_Delay(x2)
Output_Sum,to = Signal_Ideal_Delay(Input_Sum)
Y = a1*y1 + a2*y2
y = Y.shape[0]
time = t1
if (np.sum(Y - Output_Sum) == 0):
	print ("Signal_Ideal_Delay is Linear System")
else:
	print ("Signal_Ideal_Delay is Non-Linear System")
"""
plt.figure(figsize=(13, 8))
ax = plt.subplot(1, 2, 1)
plt.stem(t1,Y,'r')
ax = plt.subplot(1,2,2)
plt.stem(t1,Output_Sum,'y')
plt.show()
"""
print ("-------------------------------------------------------------------------------")

y1,t1 = Moving_Average_System(x1)
y2,t2 = Moving_Average_System(x2)
Output_Sum,to = Moving_Average_System(Input_Sum)

Y = a1*y1 + a2*y2
y = Y.shape[0]
time = np.arange(y)
	
if (round(np.sum(Y - Output_Sum)) == 0):
	print ("Moving_Average_System is Linear System")
else:
	print ("Moving_Average_System is Non-Linear System")
"""
plt.figure(figsize=(13, 8))
ax = plt.subplot(1, 2, 1)
plt.stem(time,Y,'r')
ax = plt.subplot(1,2,2)
plt.stem(time,Output_Sum,'y')
plt.show()
"""
print ("-------------------------------------------------------------------------------")

y1,t1 = Backward_Differencing_System(x1)
y2,t2 = Backward_Differencing_System(x2)
Output_Sum,to = Backward_Differencing_System(Input_Sum)

Y = a1*y1 + a2*y2
y = Y.shape[0]
time = np.arange(y)
	
if (round(np.sum(Y - Output_Sum)) == 0):
	print ("Backward_Differencing_System is Linear System")
else:
	print ("Backward_Differencing_System is Non-Linear System")
"""
plt.figure(figsize=(13, 8))
ax = plt.subplot(1, 2, 1)
plt.stem(time,Y,'r')
ax = plt.subplot(1,2,2)
plt.stem(time,Output_Sum,'y')
plt.show()
"""
print ("-------------------------------------------------------------------------------")

y1,t1 = Filter_1(x1)
y2,t2 = Filter_1(x2)
Output_Sum,to = Filter_1(Input_Sum)

Y = a1*y1 + a2*y2
y = Y.shape[0]
time = np.arange(y)
	
if (round(np.sum(Y - Output_Sum)) == 0):
	print ("y[n] = x[n] - 2x[n-1] + x[n-2] is Linear System")
else:
	print ("y[n] = x[n] - 2x[n-1] + x[n-2] is Non-Linear System")
"""
plt.figure(figsize=(13, 8))
ax = plt.subplot(1, 2, 1)
plt.stem(time,Y,'r')
ax = plt.subplot(1,2,2)
plt.stem(time,Output_Sum,'y')
plt.show()
"""
print ("-------------------------------------------------------------------------------")

y1,t1 = Filter_2(x1)
y2,t2 = Filter_2(x2)
Output_Sum,to = Filter_2(Input_Sum)

Y = a1*y1 + a2*y2
y = Y.shape[0]
time = np.arange(y)
	
if (round(np.sum(Y - Output_Sum)) == 0):
	print ("y[n] = x[2-n] + x[n-2] is Linear System")
else:
	print ("y[n] = x[2-n] + x[n-2] is Non-Linear System")
"""
plt.figure(figsize=(13, 8))
ax = plt.subplot(1, 2, 1)
plt.stem(time,Y,'r')
ax = plt.subplot(1,2,2)
plt.stem(time,Output_Sum,'y')
plt.show()
"""
print ("-------------------------------------------------------------------------------")

y1 = Squarer_System(x1)
y2 = Squarer_System(x2)
Output_Sum = Squarer_System(Input_Sum)

Y = a1*y1 + a2*y2
y = Y.shape[0]
time = np.arange(y)
	
if (round(np.sum(Y - Output_Sum)) == 0):
	print ("Squarer_System is Linear System")
else:
	print ("Squarer_System is Non-Linear System")
"""
plt.figure(figsize=(13, 8))
ax = plt.subplot(1, 2, 1)
plt.stem(time,Y,'r')
ax = plt.subplot(1,2,2)
plt.stem(time,Output_Sum,'y')
plt.show()
"""
print ("-------------------------------------------------------------------------------")
