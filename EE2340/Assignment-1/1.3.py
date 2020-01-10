import numpy as np

# Considering Input from User
num_trails = int(input("Enter Number of Trails: "))

# Printing Benroulli Random Variable num_trails times
while (num_trails):
	y = np.random.rand()
	x = int(np.round(y))
	print (x)
	num_trails -= 1
