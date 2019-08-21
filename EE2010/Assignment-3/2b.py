from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.genfromtxt('Wedge_Capacitor.csv',delimiter=',')				# Reading Data from .csv file
print ("Intial Data :\n",data)
data_test = data
numcols = data_test.shape[1]											# No.of columns in dataset
numrows = data_test.shape[0]											# No.of rows in dataset

print ("--------------------------------------------------------------")

conv = 0.5*np.array([[1],[0],[1]])										# Defining Convolution Matrix
print ("Convolution Matrix :\n",conv)

print ("--------------------------------------------------------------")

Threshold = 1															# Assigning Threshold

def Iterations(data,conv,N,t,r,c):										# Function to Iterate and generate a Heat Map
	"""
	Performing Convultion of 2 Martices
	"""
	Error = np.zeros([N,2])
	p = 1
	
	for i in range(N):
		grad = signal.convolve2d(data, conv, boundary='symm', mode='valid')
		
		data[1:r-1,0:c] = grad
		
		s = np.square(grad-t)
		RMS = np.sqrt(s.mean())
		x = np.zeros(2)
		x[0],x[1] = RMS,i
		Error[i] = x
		#plt.scatter(i,RMS)
		#plt.scatter
	
		if (abs(Error[i-100][0] - Error[i][0]) < 10**(-4) and p == 1):
			convergence = i
			p = 0
		
	#plt.plot(Error[:,1],Error[:,0],label="RMS Error")
	#plt.figure(figsize=(10,6))
	#sns.heatmap(data,cmap='YlOrBr',annot=False)						# Generating a Heat Map and not denoting the values					
	#plt.show()
	
	return data,convergence
	
data_test = (Iterations(data_test,conv,10000,Threshold,numrows,numcols))[0]
x = np.arange(numcols)
""" Divided 45 degrees into 90 parts. """
plt.plot(x,data_test[46])												# Plotting for angle 22.5 degrees
plt.show()
