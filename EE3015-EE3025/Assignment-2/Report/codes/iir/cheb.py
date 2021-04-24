import numpy as np

def cheb(N):
	v = np.array([1,0])
	u = np.array([1])
	
	if N == 0:
		w = u
	elif N == 1:
		w = v
	else:
		for i in range(1,N):
			p = np.convolve(np.array([2,0]), v);
			
			m = p.shape[0]
			n = u.shape[0]
			
			w = p + np.append(np.zeros((m-n,)), u)
			
			u = v
			v = w
			
	return w
