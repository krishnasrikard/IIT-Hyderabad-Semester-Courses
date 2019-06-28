module Project(output wire [7:0] y, input wire [31:0] x);
wire sel;
reg clk;

always #5 clk = ~clk;
wire [7:0] a;
wire [7:0] b;
wire [7:0] c;
reg [7:0] o;
wire [7:0] addr;
reg [7:0] store [255:0];

integer k;

assign sel = x[31];
assign a = x[15:8];
assign b = x[7:0];
assign c = x[23:16];

always @(sel or a or b)
begin
	if (sel == 0)
		begin 
			o = a & b;
		end
		
	else
		begin
			o = a + b;
		end
		
	k = c;
	
end

always@(*)
begin
	store[k] = o;
end

assign y = store[k];

endmodule
