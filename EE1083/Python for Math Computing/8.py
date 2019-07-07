import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x = np.linspace(1,4,100)

y1 = 1-x
y2 = x**2 - 5*x + 4
X = np.concatenate([x,x[::-1]])
Y = np.concatenate([y1,y2[::-1]])

f, a = plt.subplots()

p1= a.fill(x,y2,color ='g')
p2= a.fill(X,Y,color = 'r')
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')

a.legend([ p1[0]],{'$A = \\left\\{(x,y)\\vert y \\geq x^2-5x+4, x + y \\geq 1, y \\leq 0\\right\\}$'}, loc='best' ,prop={'size':11})
plt.show() 
