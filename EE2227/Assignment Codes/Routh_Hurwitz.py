import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cmath
from matplotlib import cm

Coeff = np.array([1,1,7,14,31,73,25,200])
#Coeff = np.array([1,2,1,2])
l = Coeff.shape[0]

RH = np.zeros((l,int(np.ceil(l/2))))
RH[0] = Coeff[0::2]

if RH.shape[1] >= Coeff[1::2].shape[0]:
	x = Coeff[1::2].shape[0]
	RH[1,:x] = Coeff[1::2]

	
for i in range(2,l):
	
	a = RH[i-2]
	b = RH[i-1]
	a1,a2 = a[0],b[0]
	for j in range(1,a.shape[0]):
		b1,b2 = a[j],b[j]
		Det = (a2*b1 - a1*b2)/a2
		RH[i][j-1] = Det
		
		t = []
		it=0
		for m in range(a.shape[0]):
			if (a[m] != 0 and b[m] != 0):
				it = it+1
				if (m==0):
					d = a[m]/b[m]
					t.append(1)
				else:
					c = a[m]/b[m]
					if (c==d):
						t.append(1)
					else:
						t.append(0)
		
	if (np.sum(t) == it and RH[i][0] == 0):
		for k in range(b.shape[0]):
			print (l-i-2*k)
			RH[i][k] = (l-i- 2*k) * b[k]
			
	elif (RH[i][0] == 0 and np.sum(t) != it):
		RH[i][0] = pow(10,-5)
		
print (RH)
