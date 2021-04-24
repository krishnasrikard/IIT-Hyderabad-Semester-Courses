function z = add(x,y)
  m = length(x);
  n = length(y);

  if m == n
      z = x + y;
  elseif m > n
      z = x + [zeros(1,m-n) y];
  else
      z = [zeros(1,n-m) x] + y;
end