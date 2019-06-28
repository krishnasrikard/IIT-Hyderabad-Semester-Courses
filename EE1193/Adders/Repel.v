
module Mux (output wire o,input wire a,b,sel);
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

endmodule
