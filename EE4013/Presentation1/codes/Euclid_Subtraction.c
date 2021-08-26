#include <stdio.h>

int SomeFunction(int x, int y){
	if ((x == 1) || (y == 1)) return 1;
	if (x == y) return x;
	if (x > y) return SomeFunction(x-y, y);
	if (x < y) return SomeFunction(x, y-x);
}

int main() {
	printf("%d\n", SomeFunction(15,255));
	return 0;
}