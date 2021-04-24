clear;
%IIR  FILTER DESIGN USING THE CHEBYSCHEV APPROXIMATION


%The order of the filter is N = 4


%Getting values of the various analog and digital filter parameters
para;

%The chebyschev filter parameter (epsilon) obtained
%from the given constraints

epsilon = 0.4;

%The analog lowpass filter
[p,G_lp] = lp_stable_cheb(epsilon,N);

Omega_L = -2:0.01:2;
H_analog_lp = G_lp*abs(1./polyval(p,j*Omega_L));
%plot(Omega_L,H_analog_lp);
%xlabel('\Omega')
%ylabel('|H_{a,LP}(j\Omega)|')

%The analog bandpass filter
[num,den,G_bp] = lpbp(p,Omega_0,B,Omega_p1);

Omega = -0.65:0.01:0.65;
H_analog_bp = G_bp*abs(polyval(num,j*Omega)./polyval(den,j*Omega));
%plot(Omega,H_analog_bp);
%xlabel('\Omega')
%ylabel('|H_{a,BP}(j\Omega)|')

%The digital bandpass filter
[dignum,digden,G] = bilin(den,omega_p1);

omega = -2*pi/5:pi/1000:2*pi/5;
H_dig_bp = G*abs(polyval(dignum,exp(-j*omega))./polyval(digden,exp(-j*omega)));
plot(omega/pi,H_dig_bp)
xlabel('\omega/\pi')
ylabel('|H_{d,BP}(\omega)|')

iir_num = G*dignum;
iir_den = digden;

%save iir_num.dat iir_num -ascii
%save iir_den.dat iir_den -ascii

save dignum.dat dignum -ascii
save digden.dat digden -ascii
%save G.dat G -ascii