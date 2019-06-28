module Mux (output wire o,input wire a,b,sel);													//Module for Mux
	assign o = (~sel&a) | (sel&b);
endmodule


module Xor (output wire o,input wire a,b);														// module for Xor
	assign o = (~b&a) | (~a&b);
endmodule


module Repel (output wire cout, output wire [7:0] s, input wire [7:0] x,y, input wire cin);		//Type of Adder

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


module Project(output wire [7:0] y, input wire [31:0] x,input wire clk);
reg sel;	
wire t,cin,s;																				//Declaring Registors and Wires
reg [7:0] a;
reg [7:0] b;
reg [7:0] r,r1;
reg [7:0] c1;
reg [7:0] o;
wire [7:0] addr,p;																			//Memory Location(Address)
reg [7:0] store [255:0];																	//Memory Element to store Data

integer k;
assign s = x[31];
assign cin = 0;

Repel j1(t,p,a,b,cin);

always @(sel)																				//Changes happening at rising edge of clock
begin
	if (sel == 0)																			//Operation regarding value of r1(sel)
		begin 
			r = a & b;																		//"AND" Operation of 2 bytes
		end
		
	else
		begin
			r = p;																			//Adding 2 bytes
		end
		
																							//Converting Binary output to an integer
end	

always @(posedge clk)																		//(Pipelining) Assigning and Propagation of values to/among registors during rising edge of clock
begin
	sel <= s;																				//Logic to select type of execution depending on even/odd byte(x[31:24])
	a <= x[15:8];
	b <= x[7:0];
	r1 <= r;
	o <= r1;
	c1 <= x[23:16];
	k <= c1;
end


always@(*)
begin
	store[k] = o;																			//Storing output in Memory
end

assign y = store[k];																		//Assigning data in memory to output wire

endmodule
