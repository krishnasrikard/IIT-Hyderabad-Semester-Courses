import numpy as np
import matplotlib.pyplot as plt

alpha = np.array([10*1e-12, 50*1e-12, 100*1e-12, 200*1e-12, 300*1e-12, 400*1e-12, 
		500*1e-12, 600*1e-12, 700*1e-12, 800*1e-12, 900*1e-12, 1*1e-9,
		2*1e-9, 3*1e-9, 4*1e-9, 5*1e-9, 6*1e-9, 7*1e-9, 8*1e-9, 9*1e-9, 10*1e-9])
		
tpout = np.array([6.9434*1e-9, 6.96226*1e-9, 7*1e-9, 7.02*1e-9, 7.1*1e-9, 7.137*1e-9,
        7.185*1e-9, 7.23491*1e-9, 7.28977*1e-9, 7.34026*1e-9, 7.39123*1e-9, 7.44*1e-9, 
        7.9*1e-9, 8.47558*1e-9, 9.00455*1e-9, 9.54167*1e-9, 1.008833*1e-8, 1.06419*1e-8, 
		1.12035*1e-8, 1.17738*1e-8, 1.23509*1e-8])

tr = 0.8*alpha
tpin = alpha/2
tp = tpout - tpin
		
plt.figure(figsize=(9,9))
plt.plot(tr,tp)
plt.grid()
plt.scatter(tr,tp)
plt.title(r"$t_{p}$ vs $t_{r,in}$")
plt.xlabel(r"$t_{r,in}$")
plt.ylabel(r"$t_{p}$")
plt.savefig("5b.png")
plt.show()
