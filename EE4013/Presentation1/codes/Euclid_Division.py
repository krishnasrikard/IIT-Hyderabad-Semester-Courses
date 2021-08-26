def SomeFunction(x,y):
	if x == 0:
		return y
	if y == 0:
		return x
	if x == y:
		return x
	if x > y:
		return SomeFunction(y, x%y)
	if x < y:
		return SomeFunction(x, y%x)

print(SomeFunction(15,255))