import numpy as np

c1 = np.roots([1,-5,4])

r1 = np.roots([1,-5,6])
print r1
r2 = np.polyval([1,4,-60],r1)
print r2
c2 = r1[np.nonzero(np.round(r2)%2==0)]
print c2

c3 = np.roots([1,4,-60])
print np.sum(c1) + np.sum(c2) + np.sum(c3)
