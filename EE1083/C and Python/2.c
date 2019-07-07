#include <stdio.h>

int main(void)
{
float a = -1.0, l = 1.0, d;
int n = 100, i;

d = (l-a)/(n-1);

for(i = 0; i < 100; i++)
{
printf("%f\n",a+i*d);
}
return 0;
}
