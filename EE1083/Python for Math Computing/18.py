import numpy as np
import scipy as sp
A = np.array ([[1,-3,-108],[1,5,-84],[1,2,-80],[1,1,-110]])

q_r = []
for i in range (0,4):
	q_r.append(np.roots(A[i,:]))

q_r = np.array(q_r)
s = q_r[q_r>0]

print s*(s-1)*(s+1)*(s+2)/np.math.factorial(6)
