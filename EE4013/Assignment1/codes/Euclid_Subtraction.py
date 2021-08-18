def SomeFunction(x,y):
	if x == 1 or y == 1:
		return 1
	if x == y:
		return x
	if x > y:
		return SomeFunction(x-y,y)
	if x < y:
		return SomeFunction(x,y-x)

print(SomeFunction(15,255))