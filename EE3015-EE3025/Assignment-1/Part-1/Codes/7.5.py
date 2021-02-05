import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def H(z,num,den):
	Num = np.polyval(num,pow(z,-1))
	Den = np.polyval(den,pow(z,-1))
	return Num/Den
	
x,fs = sf.read('Sound_Noise.wav')
order = 10
fc = 4000.0
Wn = fc/fs
print ("Wn =",Wn)

# Filter Design
num, den = signal.butter(4, Wn, 'low', analog=False)
w = np.linspace(-np.pi,np.pi,len(x),endpoint=True)
H = H(np.exp(1j*w),num,den)

# Input in Frequency Domain
X = np.fft.fftshift(np.fft.fft(x))

# Output in Freqency Domain
Y = np.multiply(H,X)
y = np.fft.ifft(np.fft.ifftshift(Y)).real
sf.write('Sound_with_ReducedNoise_7.2.wav',y,fs)
