#include <stdio.h>

float a_n(float,float,int);
float c_d(float,float,int);

int main(void)
{
float a = -1.0, l = 1.0, d;
int n = 100, i;
d = c_d(a,l,n);

for(i = 0; i<100 ;i++)
{
printf("%f\n",a_n(a,d,i));
}

return 0;
}
float a_n(float a,float d,int i)
{
return a+i*d;
}
float c_d(float a,float l,int n)
{
float d;
d = (l-a)/(n-1);
return d; 
}
