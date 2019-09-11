
"""
def square_wave(a,b,T = 1):
	n = 100*T
	print (n)
	time = np.arange(a,b,0.01)
	o = time.shape[0]
	output = np.zeros(o)
	p,q = np.ones(int(n/2)), -1*np.ones(int(n/2))
	s = np.concatenate((p,q))

	

	
	for j in range(o):
		for t in time:
			i = 1
			if (t >= 0):
				while (i > 0 and i < t/T):
					if (t-i*T < T and t-i*T > 0):
						output[j] = s[t-i*T]
						break
					i = i+1
					
			else:
				while (i > 0 and i < t/T):
					if (t+i*T < T and t+i*T > 0):
						output[j] = s[t+i*T]
						break
					i = i+1
			
		
	plt.xlabel("Time")
	plt.ylabel("Square Wave")
	plt.plot(time,output)
	plt.show()
		
	return output,time	

square_wave(0,1)
