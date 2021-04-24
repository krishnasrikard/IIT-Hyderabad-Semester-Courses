%THIS PROGRAM GENERATES THE CHEBYSCHEV POLYNOMIAL COEFFICIENTS OF ORDER N
function w = cheb(N)
  v = [1 0];
  u = 1;

  if N == 0, 
      w = u;
  elseif  N == 1, 
      w = v;
  else
    for i = 1:N-1
      p = conv([2 0],v);
      m = length(p);
      n = length(u);
        
      w =  p + [zeros(1,m-n) u];
      u = v;
      v = w;
    end
  end
end