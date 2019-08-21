from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.genfromtxt('class.csv',delimiter=',')							# Reading Data from .csv file
print ("Intial Data :\n",data)
data_test = data

print ("--------------------------------------------------------------")

conv = 0.25*np.array([[0,1,0],[1,0,1],[0,1,0]])							# Defining Convolution Matrix
print ("Convolution Matrix :\n",conv)

Threshold = 2.5															# Assigning Threshold

def Iterations(data,conv,N,t):											# Function to Iterate and generate a Heat Map
	"""
	Performing Convultion of 2 Martices
	"""
	Error = np.zeros([N,2])
	print (np.shape(Error))
	
	for i in range(N):
		grad = signal.convolve2d(data, conv, boundary='symm', mode='valid')
		data[1:6,1:6] = grad
		
		s = np.square(grad-t)
		RMS = np.sqrt(s.mean())
		x = np.zeros(2)
		x[0],x[1] = RMS,i
		Error[i] = x
		plt.scatter(i,RMS)
		
	
	plt.plot(Error[:,1],Error[:,0],label="RMS Error")
	plt.figure(figsize=(6,4))
	sns.heatmap(data,cmap='YlOrBr',annot=True)							
	plt.show()
	

Iterations(data_test,conv,20,Threshold)
