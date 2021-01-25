import numpy as np
import matplotlib.pyplot as plt

N = 15

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

plt.figure()
plt.grid()
plt.stem(h(N))
plt.xlabel('n')
plt.ylabel('h(n)')
plt.title("Filter Impulse Response")
plt.show()
