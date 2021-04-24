import numpy as np

def lp_stable_cheb(epsilon,N):
	"""
	This function gives the low pass stable filter
	for the Chebyschev approximation based upon
	the design parameters epsilon and N
	H(s) = G/p(s)
	[p,G] = lp_stable_cheb(epsilon,N)

	%Analytically obtaining the roots of the Chebyschev polynomial
	%in the left half of the complex plane
	"""
	
	beta = pow(((np.sqrt(1+ pow(epsilon,2))+ 1)/epsilon),(1/N))
	r1 = (pow(beta,2)-1)/(2*beta)
	r2 = (pow(beta,2)+1)/(2*beta)
	
	"""
	Obtaining the polynomial approximation for the low pass Chebyschev filter to obtain a stable filter
	"""
	u = 1
	for n in range(int(N/2)):
		phi = np.pi/2 + (2*n+1)*np.pi/(2*N)
		v = np.array([1, -2*r1*np.cos(phi), pow(r1*np.cos(phi),2) + pow(r2*np.sin(phi),2)])
		p = np.convolve(v,u)
		u = p
		
	G = np.abs(np.polyval(p,1j))/np.sqrt(1 + pow(epsilon,2))
	return p,G
