import numpy as np
import mpmath as mp
##import scipy
##import scipy.stats as sp
import matplotlib.pyplot as plt
##import subprocess

def recr(n,x):
	if n%3==1:
		return (x-1.0)/x;

	elif n%3==2:
		return x;

a=recr(100,3)
b=recr(1,2.0/3.0)
c=recr(2,3.0/2.0)

print (a,b,c)

Sum=a+b+c

print (Sum)
