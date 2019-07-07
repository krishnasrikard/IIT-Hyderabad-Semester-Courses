#include <stdio.h>
#include <math.h>

int main(void)
{
FILE *fp;

float x,a,b,t;
int i;

fp = fopen("16_14(new).dat","w");
 
for (i = 4;i < 10; i++)
{
x = i/8.0;
a = sqrt(2*x + 1);
b = sqrt(2*x - 1);
 
t = (a - b -1);
 
fprintf(fp,"%f\n",t);
}
fclose(fp);
return 0;
}
