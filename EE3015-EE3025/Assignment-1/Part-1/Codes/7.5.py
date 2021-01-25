import soundfile as sf
import numpy as np
from scipy import signal

def H(z,num,den):
	Num = np.polyval(num,pow(z,-1))
	Den = np.polyval(den,pow(z,-1))
	return Num/Den
	
x,fs = sf.read('Sound_Noise.wav')
order = 10
fc = 5000.0
Wn = 2*fc/fs

num,den = signal.butter(order,Wn,'low')
w = np.linspace(-Wn,Wn,len(x),endpoint=True)
z = np.exp(1j * w)

H = H(z,num,den)
X = np.fft.fft(x)

Y = np.multiply(H,X)
y = np.fft.ifft(Y).real

sf.write('Sound_with_ReducedNoise_7.5.wav',y,fs)


