import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def H(z,num,den):
	Num = np.polyval(num,pow(z,-1))
	Den = np.polyval(den,pow(z,-1))
	return Num/Den
	
x,fs = sf.read('Sound_Noise.wav')
order = 4
fc = 4000.0
Wn = 2*fc/fs
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

# Plotting
w = np.linspace(-np.pi,np.pi,len(x),endpoint=True)
plt.plot(w, abs(X)/np.max(abs(X)),label="X",color='blue')
plt.plot(w, abs(H)/np.max(abs(H)),label="H",color='red')
plt.plot(w, abs(Y)/np.max(abs(Y)),label="Y",color='green')
plt.axvline(Wn, color='black')
plt.axvline(-Wn, color='black')
plt.title('Input,Filter and Output')
plt.xlabel(r'$\omega$')
plt.legend()
plt.grid()
plt.show()
