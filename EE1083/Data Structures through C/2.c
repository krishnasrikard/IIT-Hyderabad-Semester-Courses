#include <stdio.h>
#include <stdlib.h>

double *linspace_pointer(double,double,int);

int main(void)
{
double a = -1.0, l = 1.0, *ap;
int n = 100,i;

ap = linspace_pointer(a,l,n);

for (i=0; i<n; i++)
printf("%lf\n",ap[i]);

return 0;
}
double *linspace_pointer(double a, double l,int n)
{
double d, *ap;
int i;

ap = (double*)malloc(n*sizeof(double));
d = (l-a)/(n-1);

for(i = 0; i <100; i++)
{
ap[i] = a+i*d;
}
return ap;

}
