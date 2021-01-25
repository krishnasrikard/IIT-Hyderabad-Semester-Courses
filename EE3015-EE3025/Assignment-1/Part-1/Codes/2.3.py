import soundfile as sf
from scipy import signal

input_signal,fs = sf.read('Sound_Noise.wav')
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/fs

num,den = signal.butter(order,Wn,'low')
output_signal = signal.filtfilt(num,den,input_signal)

sf.write('Sound_with_ReducedNoise.wav',output_signal,fs)
