import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cmath
from matplotlib import cm

Coeff = [1,1,7,14,31,73,25,200]
Roots = np.roots(Coeff)
print ("Roots of Polynomial Function",Roots)

plt.axhline(y=0, color='black',linewidth=0.5)
plt.axvline(x=0, color='black',linewidth=0.5)
plt.scatter(Roots.real,Roots.imag,color='red')
plt.show()

def Complex(Data,Coeff):
	Output = np.zeros(Data.shape) + 1j * np.zeros(Data.shape)
	for i in range(Data.shape[0]):
		for j in range(Data.shape[1]):
			Value = 0
			s = Data[i][j]
			for k in range(len(Coeff)):
				x = len(Coeff)
				Value += Coeff[k] * pow(s,x-k-1)
			Output[i][j] = Value
		
	return Output
		
x = np.linspace(-2.5,2.5,100)
y = np.linspace(-2.5,2.5,100)
xx, yy = np.meshgrid(x, y)

z = xx + 1j *yy

Output = Complex(z,Coeff)

surf = plt.contour(xx,yy,Output.real,colors='red')
plt.clabel(surf, inline=True, fontsize=8,colors='red')

surf = plt.contour(xx,yy,Output.imag,colors='blue')
plt.clabel(surf, inline=True, fontsize=8,colors='blue')

plt.title("Contour Map for Real(Red) and Imaginary(Blue) Parts of f(z)")
plt.xlabel('Real Part of z')
plt.ylabel('Imaginary Part of z')
plt.legend
plt.scatter(Roots.real,Roots.imag,color='black')
plt.show()
