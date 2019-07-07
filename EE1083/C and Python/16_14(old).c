#include <stdio.h>
#include <math.h>

int main(void)
{
FILE *fp;
float a,x;
int i;

fp = fopen("test.dat","w");

for(i = 0; i<21; i++)
{
x = M_PI + i;
	
a = 4 + 0.5*pow(4,(pow(2,sin(2*x))) - 2*(cos(x)));

fprintf(fp,"%f\n",a);

}
fclose(fp);
return 0;
}




