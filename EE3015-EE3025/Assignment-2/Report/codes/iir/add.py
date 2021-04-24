import numpy as np

def add(x,y):
	x = np.array(x)
	y = np.array(y)
	
	m = x.shape[0]
	n = y.shape[0]
	
	if m == n:
		z = x + y
	elif m > n:
		z = x + np.append(np.zeros((m-n,)), y)
	else:
		z = y + np.append(np.zeros((n-m,)), y)
	
	return z
