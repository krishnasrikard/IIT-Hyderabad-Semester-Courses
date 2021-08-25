#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double** createMatrix(int m,int n){
    double **a;

    a = (double **)malloc(m * sizeof(*a));
    for (int i=0;i<m;i++)
	    a[i] = (double *)malloc(n * sizeof(*a[i]));
	return a;
}

void AssignElements(double **a){
    // First Row
    a[0][0] = 3;
    a[0][1] = 0;
    a[0][2] = 1;

    // Second Row
    a[1][0] = -2;
    a[1][1] = -2;
    a[1][2] = 1;

    // Third Row
    a[2][0] = 8;
    a[2][1] = 2;
    a[2][2] = 1;
}


int main(){
    int m=3,n=3;
    double **a,  **c;
    a = createMatrix(m,n);
    AssignElements(a);
    c = createMatrix(m,n);

    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            for(int k=0;k<m;k++)
                c[i][j] = c[i][j] + a[i][k]*a[j][k];


    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            printf("%f ", c[i][j]);
        printf("\n");
}