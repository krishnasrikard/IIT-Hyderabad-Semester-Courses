
load genSpreadSpectrum.mat %z is the two messages m1, m2 interleaved backwards; 
% .mat file is backwards compatible to Matlab Version 5 or later

m1 = z(end-1:-2:1); 
m2 = z(end:-2:1);
%soundsc(m1,44100); %listen to message 1
%soundsc(m2,44100); %listen to message 2

fs = 200e3;
%bandlimit to +/- 2 kHz, upsample to 200 kHz
M1 = real(ifft(ifftshift([zeros(1,779500) fftshift(fft(m1)).*[zeros(1,200500) ones(1,40001) zeros(1,200500)] zeros(1,779500)])));
%soundsc(M1,fs); %now listen to message 1
M2 = real(ifft(ifftshift([zeros(1,779500) fftshift(fft(m2)).*[zeros(1,200500) ones(1,40001) zeros(1,200500)] zeros(1,779500)])));
%soundsc(M2,fs); %now listen to message 2

PSEUDO = ceil(rem(sqrt(reshape(1:5000,500,10).^pi+exp(1)),.01)*2000);

LPF = [ones(1,20001) zeros(1,2e6-4e4-1) ones(1,20000)];
FREQ = (12:4:88)*1000; %channel center frequencies

seed1 = 443;
seed2 = 191;

Y = zeros(1,fs*10);
t = (0:fs*10-1)/fs;

%two messages undergo frequency hopping every 1 sec. hop sequence
%determined by PSEUDO(seed,:). channels 1:1:20 are centered at 12:4:88 kHz.
for i = 1:10
    Y((i-1)*fs+1:i*fs) = M1((i-1)*fs+1:i*fs).*cos(2*pi*FREQ(PSEUDO(seed1,i))*t((i-1)*fs+1:i*fs)) ...
        + M2((i-1)*fs+1:i*fs).*cos(2*pi*FREQ(PSEUDO(seed2,i))*t((i-1)*fs+1:i*fs)); 
end
Y = Y + 0.001*randn(size(Y)); %add some noise

clear z m1 m2 M1 M2 i

Noise1 = real(ifft(fft(randn(size(Y))).*LPF));
Noise1 = Noise1.*cos(2*pi*FREQ(11)*t);
Jam1 = Noise1*sqrt(.05/sum(Noise1.^2)*fs);

Noise2 = real(ifft(fft(randn(size(Y))).*[ones(1,400001) zeros(1,2e6-80e4-1) ones(1,400000)]));
Noise2 = Noise2.*cos(2*pi*50e3*t);
Jam2 = Noise2*sqrt(.05/sum(Noise2.^2)*fs);

clear Noise1 Noise2
