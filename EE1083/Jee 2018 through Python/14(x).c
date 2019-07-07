#include <stdio.h>
#include <math.h>

int main(void)
{
	FILE *fp;
float x;
int i;

fp = fopen("17(x).dat","w");

for (i = 0; i<21; i++)
{
x = i;

fprintf(fp,"%f\n",x);
}
return 0;
}
