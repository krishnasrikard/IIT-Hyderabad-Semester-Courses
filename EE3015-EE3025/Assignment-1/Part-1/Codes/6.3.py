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

def DFT(s):
	S = []
	N = len(s)
	for k in range(N):
		o = 0 * 1j
		for n in range(N):
			o += s[n] * np.exp(-1j*2*np.pi*k*n/N)
		S.append(o)
	return S
	
def IDFT(S):
	s = []
	N = len(S)
	for n in range(N):
		o = 0 * 1j
		for k in range(N):
			o += S[k] * np.exp(1j*2*np.pi*k*n/N)
		s.append(o/N)
	s = list(np.array(s).real)
	return s

	
x = [1,2,3,4,2,1]
N = 14
h = h(N)

if (len(h) > len(x)):
	x += (len(h) - len(x))*[0]
else:
	h += (len(x) - len(h))*[0]
	
X = DFT(x)
H = DFT(h)
Y = np.multiply(X,H)
y = IDFT(Y)

plt.figure()
plt.grid()
plt.stem(y)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title("Filter Output using DFT")
plt.show()

