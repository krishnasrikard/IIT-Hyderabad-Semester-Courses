#include <stdio.h>
#include <math.h>

int main(void)
{
FILE *fp;

double x,y;
int i;

fp = fopen("1(y).dat","w");

for (i = -30 ; i < 40; i++)
{

x = i/10.0;
y = pow(x,2);

fprintf(fp,"%f\n",y);

}
return 0;
}
