#include <stdio.h> 
#include <complex.h>
#include <math.h>

# define Pi 3.141592653589793238

void fft(complex double* Signal, int N){
    if (N == 1)
        return;
    
    int P = N/2;
    complex double EvenComponents[P], OddComponents[P];

    // Splitting to Even and Odd Compoenets of Signal
    for(int i=0;i<P;i++){
        EvenComponents[i] = Signal[2*i];
        OddComponents[i] = Signal[2*i + 1];
    }

    fft(EvenComponents, P);
    fft(OddComponents, P);

    double theta;
    complex double omega;

    for(int i=0;i<P;i++){
        theta = 2*Pi*i/(double)N;
        omega = CMPLX(cos(theta), -sin(theta));

        Signal[i] = EvenComponents[i] + (omega * OddComponents[i]);
        Signal[i+P] = EvenComponents[i] - (omega * OddComponents[i]);
    }
    return;
}

void FFT(double *InputSignal, int n, complex double* FFT_InputSignal, int N){
    
    for(int i=0;i<N;i++){
        if (i < n)
            FFT_InputSignal[i] = CMPLX(InputSignal[i],0);
        else
            FFT_InputSignal[i] = CMPLX(0,0);
    }

    // Calculating Fast Fourier Transform in Recursive Fashion
    fft(FFT_InputSignal, N);
}

void h_Generation(double* h, int N){
    for(int i=0;i<N;i++){
        h[i] = pow(-0.5,i);
        if (i>=2)
            h[i] += pow(-0.5, i-2);
    }
    return;
}

void main(){
    int N,n,k;

    // FFT of x[n]
    double x[] = {1,2,3,4,2,1};
    n = sizeof(x)/sizeof(x[0]);
    // Padding Signal
    k = pow(2,ceil(log2(n)));
    if (k >= n)
        N = k;
    complex double X[N];
    FFT(x, n, X, N);

    FILE *fp;
    fp = fopen("FFTx.dat","w");
    for(int i=0;i<N;i++){
        fprintf(fp, "%lf %lf\n", creal(X[i]), cimag(X[i]));
    }
    fclose(fp);

    // FFT of h[n]
    n = 250;
    double h[n];
    h_Generation(h,n);
    // Padding Signal
    k = pow(2,ceil(log2(n)));
    if (k >= n)
        N = k;
    complex double H[N];
    FFT(h, n, H, N);
    
    fp = fopen("FFTh.dat","w");
    for(int i=0;i<N;i++){
        fprintf(fp, "%lf %lf\n", creal(H[i]), cimag(H[i]));
    }
    fclose(fp);
}