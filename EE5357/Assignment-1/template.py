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

    return(h)

def simulate_pilotestimation(n,no_trials):

    mse = np.zeros(5)
    sigmasquare = [0,0.2,0.5,1,3]
    for s in range(5):
        for i in range(no_trials):
            h,y,x = simulate_pilottransmission(n,sigmasquare[i])
            hhat = estimator(x,y,sigmasquare[i])
            mse[s] = np.sum(h-hhat)**2 / no_trials
        
    plt.plot(sigmasquare,mse)
    plt.xlabel('Noise variance')
    plt.ylabel('MSE')
    plt.grid(True)
    plt.show()


#################################################

n = 10
no_trials = 1000
print(simulate_pilotestimation(n,no_trials)
