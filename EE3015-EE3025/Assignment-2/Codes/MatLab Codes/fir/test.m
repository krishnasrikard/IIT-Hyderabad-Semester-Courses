clear;

%THIS PROGRAM FINDS THE FIR COEFFICIENTS FOR A BANDPASS FILTER USING THE
%KAISER WINDOW AND THE DESIGN SPECIFICATIONS

clear;
close;

%Filter number
L = 114;

%Sampling freqency (kHz)
Fs = 48; 

%Constant used to get the normalized digital freqencies
const = 2*pi/Fs;

%The permissible filter amplitude deviation from unity
delta = 0.15;

%Bandpass filter specifications (kHz)

%Passband F_p2 < F_p1
F_p1 = 3 + 0.6*(L-107);
F_p2 = 3 + 0.6*(L-109);

%Transition band
delF = 0.3;

%Stopband F_s2 < F_p21; F_p1 < F_s1
F_s1 = F_p1 + 0.3;
F_s2 = F_p2 - 0.3;

%Normalized digital filter specifications (radians/sec)
omega_p1 = const*F_p1;
omega_p2 = const*F_p2;

omega_c = (omega_p1+omega_p2)/2;
omega_l = (omega_p1-omega_p2)/2;

omega_s1 = const*F_s1;
omega_s2 = const*F_s2;
delomega = 2*pi*delF/Fs;


%The Kaiser window design
A = -20*log10(delta);
N = ceil((A-8)/(4.57*delomega));
%N = ceil(0.9222*pi/delomega);

N = 100;
n = -N:N;
hlp = sin(n*omega_l)./(n*pi);
hlp(N+1) = omega_l/pi;
%G = 1/sum(hlp);
%hlp = G*hlp;
%stem(hlp)

%The Bandpass filter
hbp = 2*hlp.*cos(n*omega_c);

%The lowpass filter plot
%omega = -pi/2:pi/200:pi/2;

%Hlp = abs(polyval(hlp,exp(-j*omega)));
%plot(omega/pi,Hlp)
%xlabel('\omega/\pi')
%ylabel('|H_{lp}(\omega)|')

%abs(polyval(hlp,exp(-j*0.015*pi)))

%The bandpass filter plot
omega = -pi/2:pi/200:pi/2;

Hbp = abs(polyval(hbp,exp(-j*omega)));
plot(omega/pi,Hbp)
xlabel('\omega/\pi')
ylabel('|H_{bp}(\omega)|')

fir_coeff = hbp;

%save fir_coeff.dat fir_coeff -ascii 
