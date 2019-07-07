import numpy as np
import matplotlib.pyplot as plt

k = np.linspace(-5,5,100)
d = np.sqrt(k**2 + k + 4)

plt.figure(1)
plt.plot(k,d,label = '$d=\\sqrt{k^2+k+4}$')
plt.text(-0.5,np.sqrt(15)/2-0.2,'$\\left(-\\frac{1}{2},d_{min}=\\frac{\\sqrt{15}}{2}\\right)$')
plt.plot(-0.5,np.sqrt(15)/2,'o')
plt.grid()
plt.legend(loc='best' ,prop={'size':11})
plt.xlabel('$k$')
plt.ylabel('$d$')

x =np.linspace(-2.5,2.5,100)
y = x**2 - 4

plt.figure(2)
plt.plot(x,y,label = '$y=x^2-4$')
plt.ylim(-6,1)
plt.xlim(-2.5,2.5)
plt.plot(np.sqrt(3.5),-0.5,'o')
plt.plot(-np.sqrt(3.5),-0.5,'o')
plt.plot(0,0,'o')
plt.text(-np.sqrt(3.5)+0.1,-0.5,'P $\\left(-\\sqrt{\\frac{7}{2}},-\\frac{1}{2} \\right)$')
plt.text(np.sqrt(3.5)-0.8,-0.5,'$\\left(\\sqrt{\\frac{7}{2}},-\\frac{1}{2} \\right)$ Q')
plt.text(0.1 ,0 ,'O (0,0)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.legend(loc='best' ,prop={'size':11})
plt.show()


