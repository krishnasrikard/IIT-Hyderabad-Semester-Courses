import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,2,1]

plt.figure()
plt.title("Digital Filter Input-Output")
plt.grid()
plt.stem(x)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()
