def Sin_Discrete(a,b,F,A = 1,f = 1):									# Generating Discrete Sinusoid
	"""
	A = Amplitude
	F = Sampling Frequency
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""	
	time = np.arange(a,b,1)
	amplitude = A*np.sin(2*np.pi*time*f/F)
	
	return amplitude,time

def Cos_Discrete(a,b,F,A = 1,f = 1):									# Generating Discrete Cosine
	"""
	A = Amplitude
	F = Sampling Frequency
	f = Frequency
	"a" and "b" are range for plotting the graph
	"""	
	time = np.arange(a,b,1)
	amplitude = A*np.cos(2*np.pi*time*f/F)
	
	return amplitude,time
