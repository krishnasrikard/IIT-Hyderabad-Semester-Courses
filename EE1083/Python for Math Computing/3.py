from mpmath import *
s = 0
for r in range (1,16):
		s += binomial(15,r)*r**2/binomial(15,r-1)
print s
r = 15
print (-2*r**3+ 45*r**2+ 47*r)/6
