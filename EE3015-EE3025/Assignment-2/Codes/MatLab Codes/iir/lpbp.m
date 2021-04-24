function [num,den,G_bp] = lpbp(p,Omega0,B,Omega_p2)

%This function transforms the lowpass stable filter obtained
%from the Chebyschev approximation to the bandpass
%equivalent
%[num,den,G] = lpbp(p,Omega0,B,Omega_p2)
%Omega0 and B are the lowpass-bandpass transformation parameters
%and Omega_p2 is the lower limit of the passband, used
%to evaluate the gain G_bp
%H(s) = G/p(s) is the stable low pass Cheybyschev approximation
%Hbp(s) = G_bp*num(s)/den(s) is the corresponding bandpass stable
%filter

  N = length(p);
  const = [1 0 Omega0^2];
  v = const;
  if N > 2
    for i = 1:N-1,
      M = length(v);
      v(M-i) = v(M-i) + p(i+1)*B^i;
      if i < N-1
        v = conv(const,v);
      end
    end
    
    den = v;

  elseif N==2,
    M = length(v);
    v(M-1) = v(M-1) + p(N)*B;
    den = v;
  else
    den = p;
  end

  num = [1 zeros(1,N-1)];
  G_bp = abs(polyval(den,j*Omega_p2)/(polyval(num,j*Omega_p2)));
  
end