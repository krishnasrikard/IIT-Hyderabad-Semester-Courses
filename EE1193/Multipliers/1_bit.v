module fa(output wire s, cout, input wire a, b, cin);
    assign s = a ^ b ^ cin;
    assign cout = (a & b) | (b & cin) | (cin & a);
endmodule

module mul(output wire e,f, input wire a,b,c,d);
	wire w;
	and(w,a,b);
	
	fa f1(e,f,w,c,d);

endmodule
