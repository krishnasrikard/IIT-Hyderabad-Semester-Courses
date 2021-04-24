%PLOTS OF THE LOWPASS CHEBYSCHEV FILTER OF ORDER N AND
%0.3184 < epsilon < 0.6197

clear;
%close;

figure;
hold
for N = 4:4,
  for epsilon = 0.35:0.05:0.6;
  %for epsilon = 0.4:0.4;
    Omega = 0:0.01:2;
    disp()
    H = 1./sqrt(1 + epsilon^2*cosh(N*acosh(Omega)).^2);
    plot(Omega,H)
  end
end
grid;
xlabel('\Omega')
ylabel('|H_{a,LP}(j\Omega)|')
gtext('\epsilon = 0.35')
gtext('\epsilon = 0.6')
hold off
