import numpy as np
import matplotlib.pyplot as plt
import math

N = int(1e6)

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

Sum = np.sum(h(N))

if Sum < math.inf:
	print ("Bounded")
else:
	print ("Unbounded")
