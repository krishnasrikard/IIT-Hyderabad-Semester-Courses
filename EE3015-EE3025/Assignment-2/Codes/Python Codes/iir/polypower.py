import numpy as np

def polypower(v,N):
	v = np.array(v)
	y = np.array([1])
	
	if N > 0:
		for i in range(1,int(N+1)):
			y = np.convolve(y,v)
	return y
