module And (output wire [7:0] o, input wire [7:0] p,q);
	genvar i;
    generate
        for(i = 0; i < 7; i = i + 1)
			begin
				and(o[i], p[i],q[i]);
			end
    endgenerate
endmodule

/*module Mux (output wire o,input wire a,b,sel);
	assign o = (~sel&a) | (sel&b);
endmodule


module Xor (output wire o,input wire a,b);
	assign o = (~b&a) | (~a&b);
endmodule


module Repel (output wire cout, output wire [7:0] s, input wire [7:0] x,y, input wire cin);

wire sel[7:0];
wire c[8:0];
assign c[0] = cin;


	genvar i;
    generate
        for(i = 0; i < 8; i = i + 1)
			begin
				Xor s0(sel[i],x[i],y[i]);
				Mux m0(c[i+1],y[i],c[i],sel[i]);
				Xor z0(s[i],sel[i],c[i]);
			end
    endgenerate

assign cout = c[8];

endmodule*/
/*module bin_to_int (output wire k, input wire [7:0] o);
k = o[0] + 2*o[1] + 4*o[2] + 8*o[3] + 16*o[4] + 32*o[5] + 64*o[6] + 128*o[7];
endmodule	*/		



module Project(output wire [7:0] y, input wire [31:0] x);

wire sel;
wire [7:0] a;
wire [7:0] b;
wire [7:0] c;
reg [7:0] o;

assign sel = x[31];
assign a = x[15:8];
assign b = x[7:0];
assign c = x[23:16];

always @ (sel or a or b)
begin
	if (sel == 0)
		begin 
			o = a & b;
		end
		
	else
		begin
			o = a + b;
		end
		
end

assign y = o;

endmodule
