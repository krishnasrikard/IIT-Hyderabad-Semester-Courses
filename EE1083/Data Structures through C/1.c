#include <stdio.h>
#include <stdlib.h>

int main(void)
{
double a = -1.0, l = 1.0, d ,*ap;
int n = 100, i;

ap = (double *) malloc(n * sizeof(double));

d = (l-a)/(n-1);

for (i = 0; i<100; i++)
{
ap[i] = a+i*d;
}
for(i = 0; i < n; i++)
printf("%lf\n",ap[i]);
free(ap);
return 0;
}
