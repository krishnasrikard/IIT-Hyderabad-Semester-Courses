#include <stdio.h>
#include <stdlib.h>

double **createMat1(int m,int n);
double **createMat2(int r,int s);
void readMat1(int m,int n,double **p);
void readMat2(int r,int s,double **q);

int main()
{
int m,n,r,s;
double **a;
double **b;
double **p;
double **q;

printf("Enter the size of the first matrix m n \n");
scanf("%d %d", &m,&n);

a = createMat1(m,n);
readMat1(m,n,a);


printf("Enter the size of the second matrix r s \n");
scanf("%d %d", &r,&s);

b = createMat2(r,s);
readMat2(r,s,b);


return 0;

int i,j;
for(i=0;i<m;i++)
{
for(j=0;j<n;j++)
printf("%f ",p[i][j] + q[i][j]);
printf("\n");
}
}


double **createMat1(int m,int n)
{
int i;
double **a;

a = (double **)malloc(m * sizeof(*a));
for (i=0; i<m; i++)
	a[i] = (double *)malloc(n * sizeof( *a[i]));
	
return a;
}

double **createMat2(int r,int s)
{
int i;
double **b;

b = (double **)malloc(r * sizeof(*b));
for (i=0; i<r; i++)
	b[i] = (double *)malloc(s * sizeof( *b[i]));
	
return b;
}


void readMat1(int m,int n,double ** p)
{
int i,j;


for(i=0;i<m;i++)
{
for(j=0;j<n;j++)
{
scanf("%lf",&p[i][j]);
}
}
}

void readMat2(int r,int s,double ** q)
{
int i,j;


for(i=0;i<r;i++)
{
for(j=0;j<s;j++)
{
scanf("%lf",&q[i][j]);
}
}
}
