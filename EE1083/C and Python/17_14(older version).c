#include <stdio.h>
#include <math.h>

int main(void)
{
FILE *fp;

float x,y,a,b,z;
int i;

fp = fopen("test.dat","w");

for (i = -8 ; i < 9; i++)
{
a = -13.0/3.0;
b = 64.0/9.0;
x = i/3.0;
y = a + sqrt(b - pow(x,2));
z = a - sqrt(b - pow(x,2));

fprintf(fp,"%f\n",y);
fprintf(fp,"%f\n",z);
}
fclose(fp);
return 0;
}
