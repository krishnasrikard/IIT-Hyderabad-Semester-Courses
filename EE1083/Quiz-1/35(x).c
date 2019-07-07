#include <stdio.h>
#include <math.h>

int main(void)
{
FILE *fp;

double x;
int i,j;

fp = fopen("35(x).dat","w");

for (j = 0; j < 2; j++)
for (i = -30 ; i < 40; i++)
{
x = i/100.0;

fprintf(fp,"%lf\n",x);
}
fclose(fp);
return 0;
}
