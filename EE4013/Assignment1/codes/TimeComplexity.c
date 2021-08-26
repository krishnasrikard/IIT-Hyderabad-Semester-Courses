#include <time.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>

// Euclid's Algorithm by Division
int EuclidDivision(int x, int y, int steps){
	if (x == 0) return y, steps+1;
	if (y == 0) return x, steps+1;
	if (x == y) return x, steps+1;
	if (x > y) return EuclidDivision(y, x%y, steps+1);
	if (x < y) return EuclidDivision(x, y%x, steps+1);
}

// Euclid's Algorithm by Subtraction
int EuclidSubtraction(int x, int y, int steps){
	if ((x == 1) || (y == 1)) return 1, steps+1;
	if (x == y) return x, steps+1;
	if (x > y) return EuclidSubtraction(x-y, y, steps+1);
	if (x < y) return EuclidSubtraction(x, y-x, steps+1);
}

int main() {
	FILE * fp;
	int gcd, steps, N;
	long double t1;
	struct timespec ts1, ts2;

	// Euclid's Subtraction
	fp = fopen("TimeComplexity_Subtraction.dat", "w");
	N = 400;

	int TestCases1[N][2];
	for(int i=0;i<N;i++){
		TestCases1[i][0] = 2;
		TestCases1[i][1] = 10*i + 1;
	}

	for(int i=0;i<N;i++){
		clock_gettime(CLOCK_REALTIME, &ts1);
		gcd, steps = EuclidSubtraction(TestCases1[i][0], TestCases1[i][1], 0);
		clock_gettime(CLOCK_REALTIME, &ts2);

		fprintf(fp,"%d %d 0.%09ld\n",TestCases1[i][0], TestCases1[i][1], ts2.tv_nsec - ts1.tv_nsec);
	}
	fclose(fp);

	// Euclid's Divison
	fp = fopen("TimeComplexity_Division.dat", "w");
	N = 40;

	long long int TestCases2[N][2];
	for(int i=0;i<N;i++){
		if (i==0){
			TestCases2[i][0] = 1;
			TestCases2[i][1] = 1;
		}
		else{
			TestCases2[i][0] = TestCases2[i-1][1];
			TestCases2[i][1] = TestCases2[i-1][0] + TestCases2[i-1][1];
		}
	}

	for(int i=0;i<N;i++){
		clock_gettime(CLOCK_REALTIME, &ts1);
		gcd, steps = EuclidDivision(TestCases2[i][0], TestCases2[i][1], 0);
		clock_gettime(CLOCK_REALTIME, &ts2);

		fprintf(fp,"%lld %lld 0.%09ld\n",TestCases2[i][0], TestCases2[i][1], ts2.tv_nsec - ts1.tv_nsec);
	}
	fclose(fp);
}