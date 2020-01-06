import numpy as np
import matplotlib.pyplot as plt
import math

def fact(n): 
	o = 1
	for i in range(2, n+1): 
		o = o * i  
	return o
	
def nCr(n,r):
    return (fact(n)/(fact(r) * fact(n - r)))
    
def Heads_Atmost(n=10,m=5,p=0.3):
	tp = 0
	for r in range(0,m+1):
		x = (nCr(n,r)) * pow(p,r) * pow(1-p,n-r)
		tp += x
	return tp

tp = Heads_Atmost()
print (tp)

