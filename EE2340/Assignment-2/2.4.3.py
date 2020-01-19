import numpy as np
import matplotlib.pyplot as plt

def Plot_Binary_Entropy():
	
	p = np.arange(0,1,0.001)
	q = 1 - p
	lp = np.log2(p)
	lq = np.log2(q)
	
	output = -1 * (np.multiply(p,lp) + np.multiply(q,lq))
	
	plt.plot(p,output)
	plt.show()
	
Plot_Binary_Entropy()
