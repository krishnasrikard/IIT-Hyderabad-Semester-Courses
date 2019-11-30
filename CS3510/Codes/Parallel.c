#include <stdio.h>
#include <omp.h>

int main()
{
	#pragma omp parallel
	{
		printf("I am Parallel Program\n");
	}
}