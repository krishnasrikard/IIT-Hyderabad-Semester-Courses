module fa(output wire s, cout, input wire a, b, cin);
    assign s = a ^ b ^ cin;
    assign cout = (a & b) | (b & cin) | (cin & a);
endmodule


module nX1_multiplier #(parameter [3:0] width = 4)(output wire [width-1:0] z, output wire cout,input wire [width-1:0] x,u, input wire d, input wire b);
	wire [width-1:0] c;
	wire [width-1:0] t;
		genvar i;
		generate
			for(i = 0; i < width; i = i + 1)
				begin
					and(t[i], x[i], b);
					fa fa1 (z[i], c[i], t[i], u[i], d);
				end
		endgenerate
    
	assign cout = c[width-1];
endmodule

module nXm_multiplier #(parameter [3:0] width1 = 4, [2:0] width2 = 3)(output wire [width1 + width2 - 1:0] s,input wire [width1 - 1:0] x,u, input wire [width2 - 1:0] y,v);
	wire [width1-1:0] c;
	wire [width1-1:0] z;
	wire [width1-1:0] t;
	reg [width2-1:0] r;
		genvar i,j;
		generate
			for(i = 0; i < width2; i = i + 1)
				begin
					for(j = 0; j < width1; j = j + 1)
						begin
							and(t[i], x[j], y[i]);
							fa fa1 (z[i], c[i], t[i], u[i], v[j]);
						end
					assign r[i] = z[0];
					assign u[width1-2:0] = z[width1-1:1];
					assign u[width1-1] = c[width1-1];	
				end
		endgenerate
assign s[width1 + width2 - 1:width2] = u;
assign s[width-1:0] = r;
endmodule
