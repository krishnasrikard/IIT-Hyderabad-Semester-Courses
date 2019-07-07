import numpy as np
A = np.array([[-4,-1],[3,1]])
B = np.dot(A,A)
print np.linalg.det(B - 2*A - np.identity(2))
