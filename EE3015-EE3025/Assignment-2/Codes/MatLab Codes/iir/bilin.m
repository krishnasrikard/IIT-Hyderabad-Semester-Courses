function [dignum,digden,G_bp] = bilin(p,om)

%This function transforms the stable bandpass  filter obtained
%from the Chebyschev approximation to the equivalent bandpass
%digital filter using the bilinear transformation
%[dignum,digden,G_bp] = bilin(p,om)
%H_bp(s) = G_bp*num(s)/den(s) is the analog bandpass filter
%obtained through the Chebyschev filter design
%H(z) = G*dignum(z)/digden(z) is digital bandpass filter
%obtained from H_bp(s) by substituting s = (z-1)/(z+1)
%G is obtained from the condition H(om) = 1

N = length(p);
const = [-1 1];
v = 1;
if N > 2,    
  for i = 1:N-1,
    v = conv(v,const);
    %v
    %p(i+1)*polypower([1 1],i)
    v = add(v,p(i+1)*polypower([1 1],i));
    %v1 = v
  end

  digden = v;

elseif N==2,

    M = length(v);
    v(M-1) = v(M-1) + p(N);
    v(M) = v(M) + p(N);
    digden = v;
else
    digden = p;
end

%alpha = polypower([1 1],(N-1)/2);
%beta = polypower([-1 1],(N+1)/2);
%dignum = conv(alpha,beta);
dignum = polypower([-1 0 1],(N-1)/2);

G_bp = abs(polyval(digden,exp(-j*om))/polyval(dignum,exp(-j*om)));