# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt

# Data from File
Data = np.array([4.094394745156418, 5.500075386257954, 0.7774734220353632, 3.8227823648904273, 1.543678073727923, 
0.6872913542060677, 4.2536556485420745, -0.5171601055063672, 3.8092066977149024, -0.9196478892665865, 
3.579994638569044, -0.3810522369124807, 3.3304622077743344, 4.162559482932509, 1.2108310103797562, 
3.8957204459040247, 6.302136688272647, 1.4894780522353475, 6.114291614764025, -0.5698934304468908, 
2.1948844899274764, 2.9986333142958417, 1.3861504797709088, 0.18700542819390598, 5.006051822545861, 
5.5196650758744426, 4.4861136072813395, -0.34437325976035316, 4.539142690942192, 3.465687020434631, 
1.8838766634783, -0.20522403683070245, 0.09414499668672005, 5.0314603234883, 3.7945765769148583, 
6.018783932196099, 3.6037547859962293, 0.4231846816004845, 2.756541289021439, 5.797051821336304, 
4.724435279047938, 2.6033552378788736, 4.710075111396204, 3.749334413938512, 0.09095607182072385, 
0.4461731795748265, 4.2178368315743455, 0.6831177660192798, -0.9954344782710737, 5.7344455188853365, 
0.20069586718101884, 2.1533612685256482, -0.5850537921344012, 2.300331787760747, 0.6993154780171675, 
2.981659762106143, 3.958209849037516, 1.072201349584682, 0.08052758497316947, 0.609090587922924, 
2.872939563191121, 2.034754130877956, 0.2973905985946863, 2.524492063781892, 5.423226047521808, 
0.15257051937012367, 3.497008161486992, 2.048126505442533, 5.0094060536086955, 4.870173557109632, 
1.7683252017400501, 2.6833141861945533, 3.234083346520488, 5.0010750918995726, 1.1971156721554082, 
2.1684192076185784, 2.1553964126197673, -0.39745900942132895, 5.49841566443907, 1.2498203317649643, 
6.266945105472206, 2.1328424869553277, 2.955317955856109, 4.379210782272645, 1.2365641575090527, 
0.4638902505309108, 2.4500077359461114, 6.077672674292991, 1.935528334692542, -0.26494605092528667, 
0.9019007153483616, -1.046979290965604, 6.049906189418307, 4.704766347238727, 5.021636168908162, 
3.318310542457076, 2.679746777347325, 5.840819657647555, 1.8504315076815872, 3.604549091742954])
Data = np.sort(Data)


# It is given the "X" is Uniformly Distributed Random Variable from [Alpha,Beta]
# Estimating Alpha, Beta and PMF
Alpha, Beta = np.min(Data), np.max(Data)
p = 1/(Beta - Alpha)
print ("Properties of PDF:")
print ("Alpha =", Alpha)
print ("Beta =", Beta)
print ("p =", p)
print ("-"*50)
print ("\n")

# PDF of given Data and also from given Information
def UniformPDF(X):
	O = []
	for x in X:
		if x >= Alpha and x <= Beta:
			O.append(p)
		else:
			O.append(0)
	return O


# Plotting PDF
plt.figure()
plt.plot([Alpha-1e-15] + list(Data) + [Beta+1e-15], UniformPDF([Alpha-1e-15] + list(Data) + [Beta+1e-15]))
plt.grid()
plt.xlabel(r'$x$')
plt.ylabel(r'$f_{X}(x)$')
plt.title("PDF of Random Variable X")
plt.show()


# Randomly Selecting Threshold, "a": x1hat, "b": x0hat from Given Conditions
Threshold = np.random.uniform(Alpha,Beta+1e-50)
a = np.random.uniform(Threshold+1e-50,Beta+1e-50)
b = np.random.uniform(Alpha,Threshold+1e-50)
print ("Initialsing Variables:")
print ("a =", a)
print ("Threshold =", Threshold)
print ("b =", b)
print ("-"*50)
print("\n")


# Lloyd-Max Quantisation
Thresholds = [Alpha, Threshold, Beta]
Xhat = [b,a]

i = 0
PrevMSE = 1e8
MSE = 1e6

while MSE < PrevMSE:
	PrevMSE = MSE
	
	# Updating Thresholds
	for j in range(1,len(Xhat)):
		Thresholds[j] = (Xhat[j-1] +  Xhat[j])/2
	
	# Updating Xhat
	MSE = 0
	for j in range(len(Xhat)):
		lowind = np.argmin(np.abs(Data - Thresholds[j]))
		highind = np.argmin(np.abs(Data - Thresholds[j+1]))
		Xhat[j] = np.sum(np.multiply(Data[lowind:highind],UniformPDF(Data[lowind:highind])))/np.sum(UniformPDF(Data[lowind:highind]))
		
		MSE +=  np.sum(np.multiply(np.square(Data[lowind:highind] - Xhat[j]),UniformPDF(Data[lowind:highind])))
		
	# Calculating MSE
	MSE = MSE/Data.shape[0]
		
	print ("Iteration-" + str(i) + " "* 5 + "MSE = " + str(MSE))
	i += 1
	
	# Plotting Thresholds and Xhat
	plt.figure(figsize=(8,6))
	plt.plot([Alpha-1e-15] + list(Data) + [Beta+1e-15], UniformPDF([Alpha-1e-15] + list(Data) + [Beta+1e-15]))
	plt.grid()
	plt.ylim(0,0.20)
	plt.xlabel(r'$x$')
	plt.ylabel(r'$f_{X}(x)$')
	plt.title(r"PDF of Random Variable X with Thresholds and $\hat{x_{i}}$")
	plt.stem(Xhat, UniformPDF(Xhat), linefmt='rx', label=r'$\hat{x_{i}}$')
	plt.stem(Thresholds, UniformPDF(Thresholds), linefmt='yx', label='Thresholds')
	plt.legend(loc='upper right')
	plt.show()
	
	
print ("\n"*2)
print ("Values of Variables after MSE Converges:")
print ("a =", Xhat[1])
print ("Threshold =", Thresholds[1])
print ("b =", Xhat[0])
print ("MSE at Convergence =", MSE)
print ("-"*50)
