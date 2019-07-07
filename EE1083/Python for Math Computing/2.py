import numpy as np

P = np.matrix([[np.sqrt(3)/2,0.5],[-0.5,np.sqrt(3)/2]])
A = np.matrix([[1,1],[0,1]])
B = np.matrix.transpose(P)
Q = np.dot(np.dot(P,A),B)
X = np.linalg.matrix_power(Q,2015)
print np.dot(np.dot(B,X),P)
