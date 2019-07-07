#include <stdio.h>
#include <math.h>

float f(float);

int main(void)
{
printf("%f\n" ,f(1.99));

return 0;
}

float f(float x)
{
float b = -1.0 ,a;
a = b-M_PI_2;

if(x<1)
{
return -x;
}
else if (x>=1 && x<= 2)
{
return a+acos(x+b);
}
else

return 0;
}
