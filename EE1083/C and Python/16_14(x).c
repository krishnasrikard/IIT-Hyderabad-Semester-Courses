#include <stdio.h>
#include <math.h>

int main(void)
{
FILE *fp;

float x;
int i;

fp = fopen("16_14(remastered).dat","w");
 
for (i = 4;i < 10; i++)
{
x = i/8.0;
fprintf(fp,"%f\n",x);
}
fclose(fp);
return 0;
}
