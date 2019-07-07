#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double **createMat(int m,int n);
void readMat(int m,int n,double **a);

int main()
{
int m,n;
double **a;

printf("Enter the size of the matrix m n \n");
scanf("%d %d", &m,&n);

printf("Enter the values of the matrix\n");
a = createMat(m,n);
readMat(m,n,a);


int i,j,k;
double c[2][2];

for(i=0;i<m;i++)
for(j=0;j<n;j++)
for(k=0;k<m;k++)
{
c[i][j] = c[i][j] + a[i][k]*a[j][k];
}


for(i=0;i<m;i++)
{
for(j=0;j<n;j++)
printf("%f ", c[i][j]);
printf("\n");
}


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

}
}
}
