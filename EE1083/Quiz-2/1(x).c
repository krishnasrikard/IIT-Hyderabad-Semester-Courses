#include <stdio.h>
#include <math.h>

int main(void)
{
FILE *fp;

double x,y,a,b,z;
int i;

fp = fopen("1(x).dat","w");

for (i = -30 ; i < 40; i++)
{

x = i/10.0;

fprintf(fp,"%f\n",x);

}
return 0;
}

