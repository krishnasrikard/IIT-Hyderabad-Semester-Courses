import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,2,1]
y = []
N  = 20

for i in range(N):
	o = 0;
	if i <= len(x) - 1:
		o += x[i]
	
	if i-2 <= len(x) - 1 and i-2 >= 0:
		o += x[i-2]

	if i-1 <= len(x) - 1 and i-1 >= 0:
		o -= 0.5*y[i-1]
		
	y.append(o)
	
plt.figure()
plt.grid()
plt.stem(y)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.show()
