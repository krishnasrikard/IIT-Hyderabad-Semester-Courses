#include <bits/stdc++.h>
using namespace std;

int SomeFunction(int x, int y){
	if ((x == 1) || (y == 1)) return 1;
	if (x == y) return x;
	if (x > y) return SomeFunction(x-y, y);
	if (x < y) return SomeFunction(x, y-x);
}

int main() {
	cout << SomeFunction(15,255) << endl;
	return 0;
}