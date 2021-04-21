import numpy as np
import matplotlib.pyplot as plt


def simulate_pilottransmission(n,sigmasquare):
    h = np.random.randn(2)
    x = np.random.choice([-1,1],n,p=[0.5,0.5])
    y = np.zeros(n)
    for i in range(n):
        y[i] = h[0]*x[i] + h[1]*x[(i-1)%n] + np.sqrt(sigmasquare) * np.random.randn()
    return(h,y,x)


def estimator(x,y,sigmasquare):
	h = np.zeros(2)
	# your code goes here
    
	n = x.shape[0]
	
	A1 = 0
	for i in range(n):
		if i == 0:
			A1 = A1 + (y[0] * x[n-1])
		else:
			A1 = A1 + (y[i] * x[i-1])
			
	A2 = np.sum(np.multiply(y,x))
	
	B = 0
	for i in range(n):
		if i == 0:
			B = B + (x[0] * x[n-1])
		else:
			B = B + (x[i] * x[i-1])
			
	C = np.sum(np.multiply(x,x))
	
	A = np.array([[A1], [A2]])
	M = np.array([[B,C],[C,B]])
	
	if np.linalg.det(M) == 0:
		Minv = np.linalg.pinv(M)
	else:
		Minv = np.linalg.inv(M)
	
	h = np.dot(Minv,A).flatten()

	return(h)

def simulate_pilotestimation(n,no_trials):

    mse = np.zeros(5)
    sigmasquare = [0,0.2,0.5,1,3]
    for s in range(5):
        for i in range(no_trials):
            h,y,x = simulate_pilottransmission(n,sigmasquare[s])
            hhat = estimator(x,y,sigmasquare[s])
            mse[s] += np.sum(h-hhat)**2 / no_trials
        
    plt.plot(sigmasquare,mse)
    plt.xlabel('Noise variance')
    plt.ylabel('MSE')
    plt.grid(True)
    plt.show()


#################################################

n = 10
no_trials = 1000
print(simulate_pilotestimation(n,no_trials))
