# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt

# Given Points
A = np.array([[1,2,7]])
B = np.array([[2,6,3]])
C = np.array([[3,10,-1]])

M = np.append(A,np.append(B,C, axis=0), axis=0)

# Plotting Figure
plt.figure(figsize=(6,6))
plt.grid()
ax = plt.axes(projection ='3d')
ax.plot3D(M[:,0], M[:,1], M[:,2])
ax.scatter(M[:,0], M[:,1], M[:,2])
plt.savefig("../figs/Plot.eps")