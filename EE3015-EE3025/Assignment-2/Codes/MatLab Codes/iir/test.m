clear;

%function [C K] = lattice(c,v)

%The function
%[C K] = lattice(N,D)
%computes the lattice parameters K and the ladder parameters C for the
%system function H(z) = N(z)/D(z), where both the numerator and denominator
%are of the same order
load dignum.dat
load digden.dat

%c = [0 0.44 0.36 0.02];
%v = [1 0.4 0.18 -0.2];

c = dignum;
v = digden;

u = fliplr(v);

m = length(v);
K(m-1) = v(m);
C = zeros(1,m);
C(m) = c(m);

while m > 1 & K(m-1) ~= 1
    
    c = c - C(m)*u;
    v = (v - K(m-1)*u)/(1 - K(m-1)^2);
    m = m - 1;
    v = v(1:m);
    c = c(1:m);

    u = fliplr(v);
    
    if m > 1 K(m-1) = v(m); end
    C(m) = c(m);
    
end