import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def H(z,num,den):
	Num = np.polyval(num,pow(z,-1))
	Den = np.polyval(den,pow(z,-1))
	return Num/Den
	
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
	
x,fs = sf.read('Sound_Noise.wav')
order = 4
fc = 4000.0
Wn = 2*fc/fs

num,den = signal.butter(order,Wn,'low')
w = np.linspace(-Wn,Wn,500,endpoint=True)
z = np.exp(1j * w)

H = H(z,num,den)
h = IDFT(H)

plt.figure()
plt.grid()
plt.plot(w,np.abs(H))
plt.xlabel(r'$\omega$')
plt.ylabel(r'$|H(e^{j\omega}|$')
plt.title("Filter Frequency Response")
plt.show()

plt.figure()
plt.grid()
plt.stem(h)
plt.xlabel('n')
plt.ylabel('h(n)')
plt.title("Filter Impulse Response")
plt.show()


