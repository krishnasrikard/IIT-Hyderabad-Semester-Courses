duration = 2;
f_sample = 44100;
t = (((0-1)*f_sample+0.5):((duration-1)*f_sample-0.5))/f_sample;

 [x1,f_sample1] = audioread("EE14,EE26.wav");
 
 y1 = x1(:,1);


[impulse,f_sample2] = audioread("Clap.wav");

y2 = impulse(:,1);

output = conv(y2,y1);

soundsc(output,f_sample);

audiowrite('Output.wav', output, f_sample);