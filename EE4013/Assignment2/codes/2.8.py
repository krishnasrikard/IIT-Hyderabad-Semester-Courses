import numpy as np
import matplotlib.pyplot as plt

A = [3,0]
B = [-2,-2]
C = [8,2]

def Condition (A, B, C):
    # Condition for Collinearity
    M = [A+[1], B+[1], C+[1]]
    if np.linalg.det(M) == 0:
        print ("Points are Collinear")
    else:
        print ("Points are not Collinear")

Condition(A, B, C)

def Plot(A, B, C):
    M = [B, A, C]
    M = np.array(M)

    plt.figure()
    plt.grid()
    plt.plot(M[:,0], M[:,1])
    plt.scatter(M[:,0], M[:,1])
    plt.savefig("../figs/Plot.svg")

Plot(A, B, C)
