import numpy as np
import matplotlib.pyplot as plt

N = 16

def h(N):
	h = []
	for i in range(N):
		o = 0;
		if i >= 0:
			o += pow(-0.5,i)
		if i-2 >= 0:
			o += pow(-0.5,i-2)
		h.append(o)
		
	return h

def Convolution(x,h):
	y = []
	for n in range(len(h) + len(x) - 1):
		o = 0
		for k in range(len(x)):
			if n-k>=0 and n-k<=len(h)-1:
				o += x[k]*h[n-k]
		y.append(o)

	return y
	
h = h(N)
x = [1,2,3,4,2,1]

y1 = Convolution(x,h)
y2 = Convolution(h,x)

if np.all(y1 == y2):
	print ("Hence Proved")
else:
	print ("Retry!!!")
