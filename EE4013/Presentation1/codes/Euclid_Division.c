#include <stdio.h>

int SomeFunction(int x, int y){
	if (x == 0) return y;
	if (y == 0) return x;
	if (x == y) return x;
	if (x > y) return SomeFunction(y, x%y);
	if (x < y) return SomeFunction(x, y%x);
}

int main() {
	printf("%d\n", SomeFunction(15,255));
	return 0;
}