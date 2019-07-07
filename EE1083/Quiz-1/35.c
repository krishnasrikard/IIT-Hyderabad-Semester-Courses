#include <stdio.h>
#include <math.h>

int main(void)
{
FILE *fp;

double x,y,a,b,z;
int i;

fp = fopen("35.dat","w");

for (i = -30 ; i < 40; i++)
{
a = (sqrt(2)+2)/8;
b = (3 + 2*sqrt(2))/64;
x = i/100.0;
y = a + sqrt(b - pow(x,2));

fprintf(fp,"%lf\n",y);

}

for (i = -30; i < 40; i++)
{
a = (sqrt(2)+2)/8;
b = (3 + 2*sqrt(2))/64;
x = -i/100.0;
z = a - sqrt(b - pow(x,2));

fprintf(fp,"%lf\n",z);
}
fclose(fp);
return 0;
}
