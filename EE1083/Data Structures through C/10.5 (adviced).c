#include <stdio.h>
#include <stdlib.h>

double **createMat(int m,int n);
void readMat(int m,int n,double **p);


int main()
{
int m,n,i,j;
double **a,**p,**c;

//double c[2][2], q[2][2];

printf("Enter the size of the matrix m n \n");
scanf("%d %d", &m,&n);

printf("Enter the values of the matrix\n");
a = createMat(m,n);
readMat(m,n,a);






return 0;
}


double **createMat(int m,int n)
{
int i;
double **a;

a = (double **)malloc(m * sizeof(*a));
for (i=0; i<m; i++)
	a[i] = (double *)malloc(n * sizeof( *a[i]));
	
return a;
}

void readMat (int m,int n,double **a)
{
int i,j;
for(i=0;i<m;i++)
{
for(j=0;j<n;j++)
{
scanf("%lf",&a[i][j]);
printf("%lf",a[i][j]);
}
}
printf("BYEEEE");
}
