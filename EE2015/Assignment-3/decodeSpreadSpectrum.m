    
%%% Spread Spectrum - Frequency Hopping %%%
% Your allies are simultaneously transmitting two messages using a frequency
% hopping spread spectrum technique. These are 10 sec transmissions that
% hop channels every 1 sec. You receive the transmission in variable Y.
% There are 20 channels, whose center frequencies are in FREQ. You know 
% what the seeds are to the pseudo-random hopping sequence (seed1, seed2) 
% of the two messages and can look up the channel sequence in the PSEUDO 
% table.

% Y      - Transmitted signal
% t      - Time vector (sec)
% fs     - Sampling frequency
% seed1  - Seed for message 1
% seed2  - Seed for message 2
% PSEUDO - Table of pseudorandom channel sequences (seed x hop_number) 
% FREQ   - Carrier frequency of channels 1-20
% LPF    - Low pass filter that extracts message from demodulated signal
% Jam1   - Jamming signal for channel 19
% Jam2   - Jamming signal for all channels

genSpreadSpectrum;  %Generates the spread spectrum signal. Make sure that 
                    %genSpreadSpectrum.mat, genSpreadSpectrum.p, and
                    %decodeSpreadSpectrum.m are all in your working
                    %directory

% Let's take a look at the frequency spectrum over time, using SPECTROGRAM
% Although we look at the entire spectrum over all time in this simple
% example, in practice the spread across the spectrum is much larger and the hopping 
% is much faster, so it is impracticle to look at the entire spectrum over 
% all time.
figure; spectrogram(Y,fs/10,0,fs/10,fs,'yaxis'); title('Transmitted Signal');

% Does the spectrogram make sense given the channel sequence?
% The hopping sequence of the two messages are independent of each other.
% Do you see a potential problem with this? What is the probability of the
% two messages NOT colliding during these 10 seconds if the hopping
% sequences are chosen independently, without memory, and with equal 
% likelihood at each channel?
PSEUDO(seed1,:) %<-- hop sequence for message 1 [FREQ(PSEUDO(seed1,:)) gives the frequencies]
PSEUDO(seed2,:) %<-- hop sequence for message 2


%%% Decoding Frequency Hopping %%%
% Decode both messages, using your knowledge of the encoding seeds. Do you 
% hear something unexpected midway through message 1? What is the phrase, 
% and why do we hear it?               

m1 = zeros(size(Y)); %<-- Write code to demodulate the frequency hopping sequence for seed1
s1 = FREQ(PSEUDO(seed1,:));

for i = 1:10
    t = linspace(i-1,i,200000);
    C1 = 2*cos(2*pi*s1(1,i) * t);
    m1(200000*(i-1)+1:200000*(i)) = Y(200000*(i-1)+1:200000*(i)) .* C1;
end

m1 = real(ifft(fft(m1).*LPF)); %Low pass filter (Leave me)
% soundsc(m1(1:8:end),fs/8)


m2 = zeros(size(Y)); %<-- Write code to demodulate the frequency hopping sequence for seed2
s2 = FREQ(PSEUDO(seed2,:))

for i = 1:10
    t = linspace(i-1,i,200000);
    C2 = 2*cos(2*pi*s2(1,i) * t);
    m2(200000*(i-1)+1:200000*(i)) = Y(200000*(i-1)+1:200000*(i)) .* C2;
end

m2 = real(ifft(fft(m2).*LPF)); %Low pass filter (Leave me)
% soundsc(m2(1:8:end),fs/8)


%%% Eavesdropping (Fixed Channel): Demodulate channel 19 only %%%
% Here, we assume that an eavesdropper is listening in on a fixed channel.
% For instance, listen in on channel 19. Qualitatively, what do you hear?

m = zeros(size(Y)); %<-- Write code to demodulate channel 19 only
f = FREQ(19);

t = linspace(0,10,2000000);
C = 2*cos(2*pi*f*t);
m = Y .* C;

m = real(ifft(fft(m).*LPF));
% beep; soundsc(m(1:8:end),fs/8); pause(10); beep; %beeps signal start and end of clip


%%% Eavesdropping (Wrong Key): Using seed = 354 %%%
% Here, we assume that you have the wrong seed. So the eavesdropper is
% demodulating some frequency hopping pattern, but not the correct ones.
% Qualitatively, what do you hear?

seed = 354;
m = zeros(size(Y)); %<-- Write code to demodulate the frequency hopping sequence for seed = 354
sw = FREQ(PSEUDO(seed,:));

for i = 1:10
    t = linspace(i-1,i,200000);
    Cw = 2*cos(2*pi*sw(1,i) * t);
    m(200000*(i-1)+1:200000*(i)) = Y(200000*(i-1)+1:200000*(i)) .* Cw;
end

m = real(ifft(fft(m).*LPF));
% beep; soundsc(m(1:8:end),fs/8); pause(10); beep; %beeps signal start and end of clip


%%% Jamming (Fixed Channel): Jamming channel 11 %%%
% Jam1 is a signal designed to jam channel 11. Supposed your enemy is trying 
% to impede your communications by transmitted noise on one of your channels. 
% What do the two decoded messages sound like? What is the effect of fixed channel jamming? 
Yj = Y + Jam1;
figure; spectrogram(Yj,fs/10,0,fs/10,fs,'yaxis'); title('Jamming (Fixed Channel)');


m1 = zeros(size(Yj)); %<-- Decode message 1 from the jammed transmission.
s1 = FREQ(PSEUDO(seed1,:));

for i = 1:10
    t = linspace(i-1,i,200000);
    C1 = 2*cos(2*pi*s1(1,i) * t);
    m1(200000*(i-1)+1:200000*(i)) = Yj(200000*(i-1)+1:200000*(i)) .* C1;
end
m1 = real(ifft(fft(m1).*LPF));
% soundsc(m1(1:8:end),fs/8) % ** Turn down your speakers/earphones!! **


m2 = zeros(size(Yj)); %<-- Decode message 2 from the jammed transmission.
s2 = FREQ(PSEUDO(seed2,:));

for i = 1:10
    t = linspace(i-1,i,200000);
    C2 = 2*cos(2*pi*s2(1,i) * t);
    m2(200000*(i-1)+1:200000*(i)) = Yj(200000*(i-1)+1:200000*(i)) .* C2;
end
m2 = real(ifft(fft(m2).*LPF));
% soundsc(m2(1:8:end),fs/8) % ** Turn down your speakers/earphones!! **


%%% Jamming (Spread Spectrum): Jamming all channels %%%
% Jam2 is a signal whose energy is spread across all channels. However,
% the energy required is proportional to the bandwidth (number of
% channels), so if we have a fixed amount of energy, the jamming energy
% per channel drops. Check that Jam2 and Jam1 have the same energy (what is
% the energy?). What do the two decoded messages sound like? What is the
% effect of spread spectrum jamming? (Is it really as bad as it looks in the spectrogram?)

Yj = Y + Jam2;
figure; spectrogram(Yj,fs/10,0,fs/10,fs,'yaxis'); title('Jamming (Spread Spectrum)');


m1 = zeros(size(Yj)); %<-- Decode message 1 from the jammed transmission.
s1 = FREQ(PSEUDO(seed1,:));

for i = 1:10
    t = linspace(i-1,i,200000);
    C1 = 2*cos(2*pi*s1(1,i) * t);
    m1(200000*(i-1)+1:200000*(i)) = Yj(200000*(i-1)+1:200000*(i)) .* C1;
end
m1 = real(ifft(fft(m1).*LPF));
soundsc(m1(1:8:end),fs/8)


m2 = zeros(size(Yj)); %<-- Decode message 2 from the jammed transmission.
s2 = FREQ(PSEUDO(seed2,:));

for i = 1:10
    t = linspace(i-1,i,200000);
    C2 = 2*cos(2*pi*s2(1,i) * t);
    m2(200000*(i-1)+1:200000*(i)) = Yj(200000*(i-1)+1:200000*(i)) .* C2;
end
m2 = real(ifft(fft(m2).*LPF));
soundsc(m2(1:8:end),fs/8)

