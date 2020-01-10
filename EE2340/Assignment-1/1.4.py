import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ndtri

# Random Variable
X = [0, 1, 2, 3]
# PMF of Random Variables
PMF = [0.1, 0.3, 0.1, 0.5]

# Random Generation of Random Variables corresponding to their PMF
Graph = np.random.choice(X, 10, p=PMF)

# Printing the Output
print ("Output of 10 Independent Events are ",Graph)

# Plotting the PMF of Random Variables
plt.stem(X,PMF)
plt.title("PMF of Random Variables 'X'")
plt.xlabel("X")
plt.ylabel("PMF")
plt.show()

# Calculating CDF of Random Variables
CDF = np.cumsum(PMF)
# Printing the CDF of Random Variables
print ("CDF of Random Variables 'X'",CDF)

# Plotting the CDF of Random Variables
plt.step(X,CDF,where='post')
plt.title("CDF of Random Variables 'X'")
plt.xlabel("x")
plt.ylabel("CDF")
plt.show()

# Plotting the CDF Inverse of Random Variables
plt.step(CDF,X,where='post')
plt.title("CDF Inverses of Random Variables 'X'")
plt.xlabel("x")
plt.ylabel("CDF Inverse")
plt.show()
