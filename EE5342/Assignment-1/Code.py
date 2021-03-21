## EE5342: Detection Theory - Assignment-1

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# Binary Hypothesis Testing using Bayes Decision Rule. 
# $10^6$ Samples for Monte-Carlo Simulation. 
# We are also considering Cost is Uniform

class BayesDecisionRule():
    def __init__(self):
        # 1000000 Samples for Monte-Carlo Simulation
        self.N = int(pow(10,6))
        self.L = 100
        
        # Hypothesis-0
        self.mu1,self.sigma1 = 3,1
        self.mu2,self.sigma2 = -1,1
        
        # Hypothesis-1
        self.YH1 = np.arange(-self.L, self.L+1, 0.001)
        self.P1 = 0.5*np.exp(-np.abs(self.YH1))
        self.P1 = self.P1/np.sum(self.P1)
      
    
    def H0(self, s):
        """
        Y's from Hypothesis-0
        """
        Y1 = np.random.normal(self.mu1,self.sigma1, (s,1))
        Y2 = np.random.normal(self.mu2,self.sigma2, (s,1))
        Y = np.append(Y1,Y2,axis=1)
        return Y
    
    
    def H1(self, s):
        """
        Y's from Hypothesis-1
        """
        Y1 = np.random.choice(self.YH1,p=self.P1, size=(s,1))
        Y2 = np.random.choice(self.YH1,p=self.P1, size=(s,1))
        Y = np.append(Y1,Y2,axis=1)
        return Y
    
    
    def Pr0(self,Y):
        """
        Probability Distribution for Hypothesis-0
        """
        p1 = norm.pdf((Y[:,0] - self.mu1)/self.sigma1)/self.sigma1
        p2 = norm.pdf((Y[:,1] - self.mu2)/self.sigma2)/self.sigma2
        return np.multiply(p1,p2)
    
    
    def Pr1(self,Y):
        """
        Probability Distribution for Hypothesis-1
        """
        p1 = 0.5*np.exp(-np.abs(Y[:,0]))
        p2 = 0.5*np.exp(-np.abs(Y[:,1]))
        return np.multiply(p1,p2)
        
        
    def GenerateY(self):
        """
        Generating Y's
        """
        self.H = np.sort(np.random.choice([0,1],p=[self.pi, 1-self.pi], size=(self.N,)))
        S = np.sum(self.H)
     
        Y_H0 = self.H0(self.N - S)
        Y_H1 = self.H1(S)
        self.Y = np.append(Y_H0, Y_H1, axis=0)

    
    def ComputeCost(self):
        """
        Computing Risk
        """
        self.Hhat = np.where(self.Ly >= self.Tau, 1, 0)
        return np.mean(np.abs(self.Hhat-self.H))
        
        
    def DecisionRule(self, pi):
        """
        Creating a Decision Rule and Calculating Risk
        """
        self.pi = pi
        
        # Threshold
        self.Tau = self.pi/(1-self.pi)
        
        # Generating Y
        self.GenerateY()
        
        # Decision Rule
        self.Ly = np.divide(self.Pr1(self.Y),(self.Pr0(self.Y) + 1e-20))
        
        # Cost
        Risk = self.ComputeCost()
        
        return Risk


# Generating Minimum Risk for different Prior Probabilities
BCR = BayesDecisionRule()
print ("Risk for p = 0.25: is", BCR.DecisionRule(0.25))

Probabilities = np.arange(0.1,0.901,0.1)
V = []
for p in Probabilities:
    V.append(BCR.DecisionRule(p))
        
f = plt.figure(figsize=(10,10))
plt.plot(Probabilities,V)
plt.xlabel(r"$\pi_{0}$")
plt.ylabel(r"V($\pi_{0}$)")
plt.title(r"Minimum Risk for different $\pi_{0}$")
plt.scatter(Probabilities,V)
plt.grid()
plt.show()
f.savefig("Graph.pdf", bbox_inches='tight')
