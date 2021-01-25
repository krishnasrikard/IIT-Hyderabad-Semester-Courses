import numpy as np
import matplotlib.pyplot as plt

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
	
x = [1,2,3,4,2,1]
N = 14
h = h(N)

if (len(h) > len(x)):
	x += (len(h) - len(x))*[0]
else:
	h += (len(x) - len(h))*[0]
	
X = np.fft.fft(x)
H = np.fft.fft(h)
Y = np.multiply(X,H)


print ("FFT of x(n)\n",X)
print()
print ("FFT of h(n)\n",H)
print()
print ("X(k)H(k)\n",Y)

y = np.fft.ifft(Y).real

plt.figure()
plt.grid()
plt.stem(y)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title("Filter Output using DFT")
plt.show()

