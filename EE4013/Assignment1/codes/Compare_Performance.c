#include <time.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>

// Euclid's Algorithm by Division
int EuclidDivision(int x, int y, int* steps){
	*steps += 1;
	if (x == 0) return y;
	if (y == 0) return x;
	if (x == y) return x;
	if (x > y) return EuclidDivision(y, x%y, steps);
	if (x < y) return EuclidDivision(x, y%x, steps);
}

// Euclid's Algorithm by Subtraction
int EuclidSubtraction(int x, int y, int* steps){
	*steps += 1;
	if ((x == 1) || (y == 1)) return 1;
	if (x == y) return x;
	if (x > y) return EuclidSubtraction(x-y, y, steps);
	if (x < y) return EuclidSubtraction(x, y-x, steps);
}

int main() {
	int TestCases[5][2] = {{319,50}, {453,369}, {263,810}, {243,929}, {508,609}};
	int gcd, steps1, steps2;
	long double t1, t2;

	// Clock
	struct timespec ts1, ts2, ts3, ts4;

	for(int i=0;i<5;i++){
		// Subtraction
		clock_gettime(CLOCK_REALTIME, &ts1);
		steps1 = 0;
		gcd = EuclidSubtraction(TestCases[i][0], TestCases[i][1], &steps1);
		clock_gettime(CLOCK_REALTIME, &ts2);

		// Division
		clock_gettime(CLOCK_REALTIME, &ts3);
		steps2 = 0;
		gcd = EuclidDivision(TestCases[i][0], TestCases[i][1], &steps2);
		clock_gettime(CLOCK_REALTIME, &ts4);

		printf("%d %d %d 0.%09ld %d 0.%09ld\n",TestCases[i][0], TestCases[i][1], steps1, ts2.tv_nsec - ts1.tv_nsec, steps2, ts4.tv_nsec - ts3.tv_nsec);
	}
}