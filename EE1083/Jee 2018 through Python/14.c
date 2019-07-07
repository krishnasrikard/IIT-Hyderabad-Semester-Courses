#include <stdio.h>
#include <math.h>

int main(void)
{
float x,y,z;
int i;

for (i = 0; i<21; i++)
{
x = i;
z = x - 4*(sqrt(x));
y = x - 8*(sqrt(x)) + 12;

if(i<10)
{
printf("%f\n", y);
}

else
{
printf("%f\n", z);
}

}
return 0;
}
