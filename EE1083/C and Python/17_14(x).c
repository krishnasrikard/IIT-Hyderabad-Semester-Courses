#include <stdio.h>
#include <math.h>

int main(void)
{
FILE *fp;

float x;
int i,j;

fp = fopen("17_14(x).dat","w");


for (j = 1 ; j < 3; j++)
for (i = -8 ; i < 9; i++)
{
x = i/3.0;

fprintf(fp,"%f\n",x);
}
fclose(fp);
return 0;

}
