import numpy as np
np.random.seed(1)
import matplotlib.pyplot as plt
import time

# Euclid's Division
def EuclidDivision(x,y,steps):
	if x == 0:
		return y, steps+1
	if y == 0:
		return x, steps+1
	if x == y:
		return x, steps+1
	if x > y:
		return EuclidDivision(y, x%y, steps+1)
	if x < y:
		return EuclidDivision(x, y%x, steps+1)


# Euclid's Subtraction
def EuclidSubtraction(x,y, steps):
	if x == 1 or y == 1:
		return 1, steps+1
	if x == y:
		return x, steps+1
	if x > y:
		return EuclidSubtraction(x-y,y, steps+1)
	if x < y:
		return EuclidSubtraction(x,y-x, steps+1)


# No.of Test Cases
Num_TestCases = 5

# Test Cases
Test_Cases = np.arange(1,int(1e3))
np.random.shuffle(Test_Cases)
Test_Cases = Test_Cases[:2*Num_TestCases].reshape(-1,2)

# Algorithm Details
Subtraction = {}
Division = {}

# Collecting Details
for t in Test_Cases:
	# Subtraction Details
	t1 = time.time()
	_, n = EuclidSubtraction(t[0], t[1], 0)
	t2 = time.time()
	Subtraction[(t[0], t[1])] = (t2-t1, n)
	
	# Division Details
	t1 = time.time()
	_, n = EuclidDivision(t[0], t[1], 0)
	t2 = time.time()
	Division[(t[0], t[1])] = (t2-t1, n)
	

Subtraction = dict(sorted(Subtraction.items(), key=lambda item: item[1][0]))

for key, value in Subtraction.items():
	print (key, value, Division[key])
