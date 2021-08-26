import numpy as np
np.set_printoptions(precision=9)
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys
sys.setrecursionlimit(int(1e4))

# Euclid's Subtraction
f = open("TimeComplexity_Subtraction.dat", "rb")
Lines = f.readlines()
X = np.zeros((len(Lines),))
y = np.zeros((len(Lines),))

for i in range(len(Lines)):
	Data = Lines[i].split()
	X[i] = (int(Data[0]) + int(Data[1]))
	y[i] = (float(Data[2]))

# Theoritical Curve of O(n)
def Linear(x,a,b):
	return a*x + b
	
# Curve Fitting
popt, pcov = curve_fit(Linear, X, y)
a = popt[0]
b = popt[1]

# Plotting Results
plt.figure()
plt.grid()
plt.plot(X,y, label="Experimental Plot")
plt.plot(X, a*X + b, label="Theoritical Curve Fit Plot")
plt.ylabel("Time")
plt.xlabel(r"a+b")
plt.title("Time Complexity")
plt.legend()
plt.savefig("../figs/Euclid_Subtraction.eps")
plt.show()


# Euclid's Division
f = open("TimeComplexity_Division.dat", "rb")
Lines = f.readlines()
X = np.zeros((len(Lines),))
y = np.zeros((len(Lines),))

for i in range(len(Lines)):
	Data = Lines[i].split()
	X[i] = (int(Data[0]) + int(Data[1]))
	y[i] = (float(Data[2]))
	
# Theoritical Curve of O(log(n))
def Log(x,k):
	return (k * np.log(x)) + 1e-10

popt, pcov = curve_fit(Log, X, y)
k = popt[0]

# Plotting Results
plt.figure()
plt.grid()
plt.plot(X,y, label="Experimental Plot")
plt.plot(X, k*np.log(X), label="Theoritical Curve Fit Plot")
plt.ylabel("Time")
plt.xlabel(r"min(a+b)")
plt.title("Time Complexity")
plt.legend()
plt.savefig("../figs/Euclid_Division.eps")
plt.show()
