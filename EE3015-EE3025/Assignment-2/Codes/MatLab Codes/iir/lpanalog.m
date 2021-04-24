clear;

figure;
hold;
%The low-pass Chebyschev design parameters
epsilon = 0.4;
N = 4;

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

%The following was to verify that the roots obtained
%are correct
%roots(p)
p1 = epsilon^2*conv(cheb(N),cheb(N)) + [zeros(1,2*N) 1];
%r = roots(p1)

%Evaluating the gain of the stable lowpass filter
%The gain has to be 1/sqrt(1+epsilon^2) at Omega = 1
G = abs(polyval(p,j))/sqrt(1+epsilon^2);

%Plotting the magnitude response of the stable filter
%and comparing with the desired response for the purpose
%of verification

Omega = 0:0.01:2;
H_stable = abs(G./polyval(p,j*Omega));
H_cheb = abs(sqrt(1./polyval(p1,j*Omega)));
plot(Omega,H_stable,'o');
plot(Omega,H_cheb);

xlabel('\Omega')
ylabel('|H_{a,LP}(j\Omega)|')
legend('Design','Specification')

hold off;