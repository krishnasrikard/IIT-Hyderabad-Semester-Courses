module test;
reg clk;
reg [7:0] s;
wire [7:0] storage;


always #10 clk=-clk;
initial begin
	clk = 1;	
	s = 8'b00000011;

end
xin d1(storage,s,clk);

initial begin
	$monitor ( "%0d", storage[7:0]);
end 

endmodule
