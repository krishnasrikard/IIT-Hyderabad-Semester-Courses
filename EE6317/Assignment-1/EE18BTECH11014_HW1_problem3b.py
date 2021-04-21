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

# Channel Coded Data with R = 2/5
def ChannelEncode(Signal):
	"""
	Encoding Data with R = n/k
	"""
	EncodeMap = {tuple([0,0]):np.array([0,0,0,0,0]), 
				tuple([0,1]):np.array([0,0,1,1,1]), 
				tuple([1,0]):np.array([1,1,1,0,0]), 
				tuple([1,1]):np.array([1,1,0,1,1])}
	EncodeKeys = list(EncodeMap.keys())
	
	n = len(EncodeKeys[0])
	k = EncodeMap[EncodeKeys[0]].shape[0]
	
	Signal = Signal.reshape(-1,n)
	N = Signal.shape[0]
	Output = np.zeros((N,k))
	
	for i in range(N):
		try:
			t = tuple(Signal[i])
		except:
			t = tuple([Signal[i]])
		Output[i] = EncodeMap[t]
		
	Output = Output.flatten().astype(int)
	return Output
	
# Encoding Data
X_Encoded = ChannelEncode(X)

# Transmit Data through Binary Channel
def Transmit(Signal,f):
	Output = []
	for i in range(Signal.shape[0]):
		Output.append(np.random.choice(2,p = f[Signal[i]]))
	return np.array(Output)
	
# Received Bits
Y = Transmit(X_Encoded,f)

# Decode Received Bits using MLE
def Decode(Signal,f):
	"""
	Decoding Data with R = n/k
	"""
	DecodeMap = {tuple([0,0,0,0,0]):np.array([0,0]), 
				tuple([0,0,1,1,1]):np.array([0,1]), 
				tuple([1,1,1,0,0]):np.array([1,0]), 
				tuple([1,1,0,1,1]):np.array([1,1])}
	DecodeKeys = list(DecodeMap.keys())
		
	L = len(DecodeKeys)
	k = len(DecodeKeys[0])
	n = DecodeMap[DecodeKeys[0]].shape[0]
	
	Signal = Signal.reshape(-1,k)
	N = Signal.shape[0]
	Output = np.zeros((N,n))

	for i in range(N):
		t = tuple(Signal[i])
		
		d = np.ones((L,))
		for j in range(L):
			Code = DecodeKeys[j]
			
			for l in range(k):
				d[j] *= f[Code[l]][t[l]]
		
		Output[i] = DecodeMap[DecodeKeys[np.argmax(d)]]
	
	Output = Output.flatten().astype(int)
	return Output

# Decoded Bits
Xhat = Decode(Y,f)

# Calculating BER
def CalculateBER(X,Xhat):
	return np.mean(np.bitwise_xor(X,Xhat))
	
# BER
print ("BER =", CalculateBER(X,Xhat))

