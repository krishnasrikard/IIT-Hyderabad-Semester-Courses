import numpy as np
import matplotlib.pyplot as plt

# Displaying Image
mss = np.load("mss.npy")
plt.figure()
plt.imshow(mss,cmap='gray')
plt.show()

# Original Bits
X = mss.flatten()

# Transmission Probability Matrix
f = np.array([[0.20488,0.79512],[0.7362,0.2638]])
print ("Transmission Probability Matrix:\n", f)
print ()

# Transmit Data through Binary Channel
def Transmit(Signal,f):
	Output = []
	for i in range(Signal.shape[0]):
		Output.append(np.random.choice(2,p = f[Signal[i]]))
	return np.array(Output)
	
# Received Bits
Y = Transmit(X,f)

# Decode Received Bits using MLE
def Decode(Signal,f):
	"""
	Only Valid if R = 1
	"""
	Output = []
	for i in range(Signal.shape[0]):
		Output.append(np.argmax(f[:,Signal[i]]))
	return np.array(Output)

# Decoded Bits
Xhat = Decode(Y,f)

# Calculating BER
def CalculateBER(X,Xhat):
	return np.mean(np.bitwise_xor(X,Xhat))
	
# BER
print ("BER =", CalculateBER(X,Xhat))
