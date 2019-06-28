module fa(output wire s, cout, input wire a, b, cin);
    assign s = a ^ b ^ cin;
    assign cout = (a & b) | (b & cin) | (cin & a);
endmodule

module nX1_multiplier (output wire [4:0] z, input wire [3:0] x,u, input wire d, input wire b);

wire [4:0] c;
wire [3:0] t;
assign c[0] = d;
	
	genvar i;
    generate
        for(i = 0; i < 4; i = i + 1)
			begin
				and(t[i], x[i], b);
				fa fa1 (z[i], c[i+1], t[i], u[i], c[i]);
            end
    endgenerate
    
assign z[4] = c[4];
endmodule

module nXm_multiplier (output wire [6:0] s,input wire [3:0] x,u, input wire [2:0] y,v, input wire clk,reset);
	wire [4:0] c;
	wire [4:0] z1,z2;
	wire [3:0] t1,t2,t3;

	
assign t1 = u;
nX1_multiplier m0(z1,x,t1,v[0],y[0]);
assign s[0] = z1[0];
	
assign t2 = z1[4:1];
nX1_multiplier m1(z2,x,t2,v[1],y[1]);
assign s[1] = z2[0];
	
assign t3 = z2[4:1];
nX1_multiplier m2(s[6:2],x,t3,v[2],y[2]);

endmodule
