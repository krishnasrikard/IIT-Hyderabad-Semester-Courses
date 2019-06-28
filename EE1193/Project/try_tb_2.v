module test;															//Test Bench
localparam width = 32;
wire [7:0] y;															//Output
reg [width-1:0] x;														//Input
reg clk;																//Clock
reg [7:0] store [255:0];												//Memory

  initial 
	begin
		clk = 1;														
	end
      
always #5 clk = ~clk;													//Generating a clock of period 5

initial begin															//Inputs ; They get asssigned during rising edge of clock
	x = 98765483280;
	#10;
	@(posedge clk);
	#10;
	x = 1234567890;
	@(posedge clk)
	#10;
	
	x = 32'b10000011110010101011111111100000;

	@(posedge clk)
		#10;
	
	
	x = 74121369850;
	@(posedge clk)
		#10;

	
	x = 1850;
	
	@(posedge clk)
		#10;

	x = 7412850;
	$finish;
end
 
Project r1(y,x,clk);													//Calling Module
  
  
initial begin
	$monitor("At time %t, %b	 %b", $time,y, x);						//Monitoring the Output
	$display("%0d",store[1]);											//Displaying the Output
end

initial begin
	$dumpfile("Project.vcd");											//Generating .vcd File
	$dumpvars;

end

endmodule


