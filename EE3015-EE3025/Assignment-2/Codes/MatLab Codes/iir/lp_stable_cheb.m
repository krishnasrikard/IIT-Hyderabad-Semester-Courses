function [p,G] = lp_stable_cheb(epsilon,N)

%This function gives the low pass stable filter
%for the Chebyschev approximation based upon
%the design parameters epsilon and N
%H(s) = G/p(s)
%[p,G] = lp_stable_cheb(epsilon,N)

%Analytically obtaining the roots of the Chebyschev polynomial
%in the left half of the complex plane

beta = ((sqrt(1+epsilon^2)+ 1)/epsilon)^(1/N);
r1 = (beta^2-1)/(2*beta);
r2 = (beta^2+1)/(2*beta);

%Obtaining the polynomial approximation for the low pass
%Chebyschev filter to obtain a stable filter
u = 1;
for n = 0:(N/2)-1;
  phi = pi/2 + (2*n+1)*pi./(2*N);
  v = [1 -2*r1*cos(phi) r1^2*cos(phi)^2+r2^2*sin(phi)^2];
  p = conv(v,u);
  u = p;
end

%Evaluating the gain of the stable lowpass filter
%The gain has to be 1/sqrt(1+epsilon^2) at Omega = 1
G = abs(polyval(p,j))/sqrt(1+epsilon^2);
%G = abs(polyval(p,j));