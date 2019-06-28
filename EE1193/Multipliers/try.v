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

module nXm_multiplier (output wire [6:0] s,input wire [3:0] x,u, input wire [2:0] y,v);
	wire [3:0] c;
	wire [4:0] z;
	wire [3:0] w;
	reg [2:0] r;
		genvar i,j;
		generate
			for(i = 0; i < 3; i = i + 1)
				begin
					assign w = u;
					nX1_multiplier mul1 (z,x,w,y[i],v[i]);
					assign s[i] = z[0];
					assign w = z[4:1];
				end
		endgenerate
assign s[6:3] = w;
endmodule
