function y = polypower(v,N)
  y = 1;
  if N > 0      
    for i = 1:N
      y = conv(y,v);  
    end
  end
end