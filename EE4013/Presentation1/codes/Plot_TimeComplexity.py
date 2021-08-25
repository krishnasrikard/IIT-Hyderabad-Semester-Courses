import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.setrecursionlimit(int(1e4))

# Euclid's Division
def EuclidDivision(x,y):
	if x == 0:
		return y
	if y == 0:
		return x
	if x == y:
		return x
	if x > y:
		return EuclidDivision(y, x%y)
	if x < y:
		return EuclidDivision(x, y%x)


# Euclid's Subtraction
def EuclidSubtraction(x,y):
	if x == 1 or y == 1:
		return 1
	if x == y:
		return x
	if x > y:
		return EuclidSubtraction(x-y,y)
	if x < y:
		return EuclidSubtraction(x,y-x)

# Euclid's Subtraction
Test_Cases = np.arange(2,int(1e3),5)

X = []
y = []
for t in Test_Cases:
	t1 = time.time()
	EuclidSubtraction(2, t)
	t2 = time.time()
	X.append(2+t)
	y.append(t2-t1)
plt.grid()
plt.plot(X,y)
plt.savefig("../figs/Euclid_Subtraction.eps")
plt.show()

# Euclid's Division
Test_Cases = [0,1]
for i in range(28):
	Test_Cases.append(Test_Cases[-1] + Test_Cases[-2])

D = {}
for i in range(0,len(Test_Cases)-1,2):
	t1 = time.time()
	EuclidDivision(Test_Cases[i], Test_Cases[i+1])
	t2 = time.time()
	D[min(Test_Cases[i], Test_Cases[i+1])] = t2-t1

X = []
y = []
for i in sorted(D):
	X.append(i)
	y.append(D[i])

plt.grid()
plt.plot(X,y)
plt.savefig("../figs/Euclid_Division.eps")
plt.show()
