#include <stdio.h>
#include <stdlib.h>

typedef struct list
{
double data;
struct list *next;
}node;

node *linspace_pointer(double,double,int);

int main(void)
{
node *ap;
double a = -1.0, l = 1.0;
int n = 100;

ap = linspace_pointer(a,l,n);

while(ap->next !=NULL)
{
printf("%lf\n", ap->data);
ap = ap->next;
}
return 0;
}

node *linspace_pointer(double a, double l,int n)
{
node *ap, *head;
double d;
int i;

d = (l-a)/(n-1);

ap = (node*)malloc(n*sizeof(node));
head = ap;

for(i = 0; i <100; i++)
{
ap->data = a+i*d;

ap->next = (node*)malloc(n*sizeof(node));

ap->next->next = NULL;

ap = ap->next;
}
return head;
}
