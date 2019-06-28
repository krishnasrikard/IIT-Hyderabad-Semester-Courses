import numpy as np
import matplotlib.pyplot as plt

A = np.array([1,0])
B = np.array([0,1])
C = np.array([-1,0])
D = np.array([0,1])
len = 1000
lam = np.linspace(-2,2,len)
x_CD = np.zeros((2,len))
x_PF = np.zeros((2,len))
x_t = np.zeros((2,len))
U = np.zeros((2,2))

def dr(AB):
	return np.matmul(AB,dvec)
	
def norm_vec(AB):
	return np.matmul(omat,np.matmul(AB,dvec))
	
dvec = np.array([-1,1])
omat = np.array([[0,1],[-1,0]])

CD = np.vstack((C,D)).T
S = dr(CD)
n = (np.linalg.norm(S))
T = norm_vec(CD)

y = (S[0]/S[1])*0.5
x = (y)**2
P = np.array([x,y])

a = S[0]
b = -S[1]
G = np.array([a,b])
d = (np.matmul(G,P) + 1)/n

print (d)

U[:,0] = S
U[:,1] = T

c = np.matmul(P,S)
d = np.matmul(C,T)

V = np.array([c,d])

F = np.matmul((np.linalg.inv(U)),V)

for i in range(len):
	
	temp1 = lam[i]*B + (lam[i]*lam[i])*A
	x_t[:,i] = temp1.T
	
	temp2 = C + lam[i]*(D-C)
	x_CD[:,i] = temp2.T
	
	temp3 = F + lam[i]*(F-P)
	x_PF[:,i] = temp3.T

plt.plot(x_t[0,:],x_t[1,:],label='$AB$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_PF[0,:],x_PF[1,:],label='$PF$')

plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1.55),P[1]*(0.75),'P')

plt.plot(F[0],F[1],'o')
plt.text(F[0]*(1.3),F[1]*(1.15),'F')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
